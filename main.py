import os
from generator import generate_mock_cloud_data
from analyzer import FinOpsAnalyzer
from ai_advisor import FinOpsAIAdvisor
from config import REPORT_OUTPUT_FILE


def main():
    print("==================================================")
    print("   AI-POWERED CLOUD FINOPS COST OPTIMIZATION AGENT")
    print("==================================================")

    # Step 1: Ensure mock telemetry exists
    if not os.path.exists("cloud_resource_metrics.csv"):
        generate_mock_cloud_data()

    # Step 2: Run rule-based waste detection
    analyzer = FinOpsAnalyzer()
    metrics = analyzer.analyze_waste()

    # Step 3: Format the metrics report
    report_lines = []
    report_lines.append("==================================================")
    report_lines.append("           CLOUD FINOPS EXECUTIVE REPORT          ")
    report_lines.append("==================================================")
    report_lines.append(f"Total Resources Scanned    : {metrics['total_resources']}")
    report_lines.append(f"Total Monthly Cloud Spend  : ${metrics['total_monthly_spend']}")
    report_lines.append(f"Flagged Wasteful Resources : {metrics['wasted_resources_count']}")
    report_lines.append(f"Potential Monthly Savings  : ${metrics['wasted_monthly_spend']}")
    report_lines.append(f"Potential Annual Savings   : ${metrics['wasted_annual_spend']}")
    report_lines.append(f"Waste Percentage of Budget : {metrics['waste_percentage']}%")
    report_lines.append("--------------------------------------------------")
    report_lines.append("RECOMMENDED ACTIONS (FLAGGED WASTE ITEMS):")
    report_lines.append("--------------------------------------------------")

    for _, row in metrics["flagged_df"].iterrows():
        action_line = (
            f"- [ID: {row['Resource_ID']}] Type: {row['Resource_Type']} | "
            f"Region: {row['Region']} | Cost: ${row['Monthly_Cost_USD']}/mo | "
            f"Reason: {row['Waste_Reason']}"
        )
        report_lines.append(action_line)

    report_lines.append("==================================================")

    metrics_text = "\n".join(report_lines)

    # Step 4: Generate executive AI summary
    print("[INFO] Generating executive AI summary...")
    advisor = FinOpsAIAdvisor()
    ai_summary = advisor.generate_executive_brief(metrics_text)

    full_output = f"{metrics_text}\n\nAI EXECUTIVE SUMMARY:\n{ai_summary}\n"
    print(full_output)

    # Step 5: Save output to report file
    with open(REPORT_OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_output)

    print(f"[SUCCESS] FinOps report successfully saved to '{REPORT_OUTPUT_FILE}'!")


if __name__ == "__main__":
    main()