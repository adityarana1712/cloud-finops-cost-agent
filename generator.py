import random
import pandas as pd
from config import RESOURCE_DATA_FILE


def generate_mock_cloud_data():
  print("[INFO] Generating mock cloud infrastructure usage data...")

  regions = ["us-east-1", "eu-west-1", "ap-south-1", "us-west-2"]
  resource_types = ["Virtual_Machine", "Block_Storage", "Database"]

  data = []
  random.seed(42)  # For consistent mock data generation

  for i in range(1, 61):  # Generate 60 cloud resources
    r_type = random.choice(resource_types)

    if r_type == "Virtual_Machine":
      res_id = f"i-vm-{1000 + i}"
      cpu_util = round(random.uniform(1.0, 95.0), 2)
      days_inactive = 0
      monthly_cost = round(random.uniform(40.0, 300.0), 2)
      # Force some VMs to be artificially idle for testing waste detection
      if i % 4 == 0:
        cpu_util = round(random.uniform(0.5, 3.5), 2)

    elif r_type == "Block_Storage":
      res_id = f"vol-disk-{2000 + i}"
      cpu_util = 0.0
      days_inactive = random.randint(0, 75)
      monthly_cost = round(random.uniform(10.0, 80.0), 2)

    else:  # Database
      res_id = f"db-rds-{3000 + i}"
      cpu_util = round(random.uniform(5.0, 85.0), 2)
      days_inactive = 0
      monthly_cost = round(random.uniform(150.0, 600.0), 2)
      if i % 7 == 0:
        cpu_util = round(random.uniform(0.1, 2.0), 2)

    data.append({
        "Resource_ID": res_id,
        "Resource_Type": r_type,
        "Region": random.choice(regions),
        "CPU_Util_Avg_Pct": cpu_util,
        "Days_Inactive": days_inactive,
        "Monthly_Cost_USD": monthly_cost,
    })

  df = pd.DataFrame(data)
  df.to_csv(RESOURCE_DATA_FILE, index=False)
  print(
      f"[SUCCESS] Mock cloud resource data saved to '{RESOURCE_DATA_FILE}'."
  )


if __name__ == "__main__":
  generate_mock_cloud_data()