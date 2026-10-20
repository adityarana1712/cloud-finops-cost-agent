# ☁️ AI-Powered Cloud FinOps Cost Optimization Agent

An automated Cloud Financial Operations (FinOps) pipeline built in Python to detect idle infrastructure, quantify recurring cost waste, and generate executive-ready AI optimization briefs using the Gemini API.

---

## 📌 Overview

Cloud over-provisioning and abandoned storage cost enterprises millions in avoidable spend each year. This tool functions as an autonomous cloud audit agent:
1. **Telemetry Ingestion:** Simulates or reads structured cloud telemetry across virtual machines, storage volumes, and managed databases.
2. **Waste Detection Engine:** Applies Pandas-driven threshold analysis to pinpoint underutilized compute instances and zombie storage volumes.
3. **AI Executive Briefings:** Uses Google's Gemini LLM to synthesize raw telemetry into high-level, actionable financial strategies tailored for technical directors, VPs of Engineering, and CFOs.

---

## 🚀 Key Features

- **Automated Waste Identification:**
  - Flags compute instances (VMs, RDS databases) idling below 5% average CPU utilization.
  - Detects unattached/inactive storage volumes (EBS/Disks) idle for 30+ days.
- **Financial Impact Modeling:** Aggregates immediate monthly savings and projected annual cost recovery.
- **Executive Summaries via Gemini:** Converts technical log metrics into actionable, strategic recommendations with next-step priorities.
- **Zero-Setup Mock Telemetry:** Includes a realistic cloud metric generator to simulate enterprise workloads out of the box.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Data Analysis:** Pandas
- **AI / LLM:** Google GenAI SDK (`gemini-3.8-flash`)
- **Version Control:** Git & GitHub

---

## 📂 Project Architecture