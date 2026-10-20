import pandas as pd
from config import (
    CPU_IDLE_THRESHOLD_PCT,
    RESOURCE_DATA_FILE,
    STORAGE_INACTIVE_DAYS,
)


class FinOpsAnalyzer:

  def __init__(self):
    try:
      self.df = pd.read_csv(RESOURCE_DATA_FILE)
    except FileNotFoundError:
      raise FileNotFoundError(
          f"[ERROR] Data file '{RESOURCE_DATA_FILE}' not found. Run generator.py"
          " first."
      )

  def analyze_waste(self):
    print("[INFO] Analyzing cloud resource utilization and cost waste...")

    # 1. Flag Idle Virtual Machines & Databases
    idle_mask = (self.df["Resource_Type"].isin(["Virtual_Machine", "Database"])) & (
        self.df["CPU_Util_Avg_Pct"] < CPU_IDLE_THRESHOLD_PCT
    )

    # 2. Flag Inactive Storage Volumes
    storage_mask = (self.df["Resource_Type"] == "Block_Storage") & (
        self.df["Days_Inactive"] > STORAGE_INACTIVE_DAYS
    )

    # Combine waste findings
    waste_df = self.df[idle_mask | storage_mask].copy()

    # Categorize the type of waste for each row
    def get_waste_reason(row):
      if (
          row["Resource_Type"] in ["Virtual_Machine", "Database"]
          and row["CPU_Util_Avg_Pct"] < CPU_IDLE_THRESHOLD_PCT
      ):
        return f"Underutilized (CPU avg {row['CPU_Util_Avg_Pct']}% < {CPU_IDLE_THRESHOLD_PCT}%)"
      elif (
          row["Resource_Type"] == "Block_Storage"
          and row["Days_Inactive"] > STORAGE_INACTIVE_DAYS
      ):
        return (
            f"Unattached/Inactive for {row['Days_Inactive']} days (Threshold:"
            f" {STORAGE_INACTIVE_DAYS}d)"
        )
      return "General Inefficiency"

    waste_df["Waste_Reason"] = waste_df.apply(get_waste_reason, axis=1)

    total_monthly_spend = self.df["Monthly_Cost_USD"].sum()
    wasted_monthly_spend = waste_df["Monthly_Cost_USD"].sum()
    waste_percentage = (
        (wasted_monthly_spend / total_monthly_spend) * 100
        if total_monthly_spend > 0
        else 0
    )

    report_data = {
        "total_resources": len(self.df),
        "total_monthly_spend": round(total_monthly_spend, 2),
        "wasted_resources_count": len(waste_df),
        "wasted_monthly_spend": round(wasted_monthly_spend, 2),
        "wasted_annual_spend": round(wasted_monthly_spend * 12, 2),
        "waste_percentage": round(waste_percentage, 2),
        "flagged_df": waste_df,
    }

    return report_data