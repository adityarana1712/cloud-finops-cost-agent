import os
from google import genai

class FinOpsAIAdvisor:
    def __init__(self):
        # Checks for GEMINI_API_KEY environment variable
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    def generate_executive_brief(self, metrics_summary_text):
        if not self.client:
            return (
                "\n[AI Advisor Note] Set GEMINI_API_KEY in your environment to auto-generate "
                "AI executive insights. Skipping AI generation for now.\n"
            )

        prompt = f"""
You are a Cloud FinOps Consultant. Review the following cloud waste scan report and write a crisp, 
executive-ready summary (3-4 bullet points) for the VP of Engineering and CFO.

Key details to cover:
1. High-level financial impact (highlight monthly and annual waste).
2. Root causes of the waste (unattached storage vs. over-provisioned compute/databases).
3. Concrete next steps: quick wins vs. architectural rightsizing.

Keep the tone professional, direct, and actionable.

Raw Report Data:
{metrics_summary_text}
"""
        try:
            response = self.client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"\n[AI Advisor Error] Failed to generate AI brief: {e}\n"