# Configuration settings for the Cloud FinOps Agent

RESOURCE_DATA_FILE = "cloud_resource_metrics.csv"
REPORT_OUTPUT_FILE = "finops_optimization_report.txt"

# Optimization Thresholds
CPU_IDLE_THRESHOLD_PCT = (
    5.0  # VMs with average CPU under 5% are flagged as idle
)
STORAGE_INACTIVE_DAYS = (
    30  # Volumes unused for over 30 days are flagged for deletion
)