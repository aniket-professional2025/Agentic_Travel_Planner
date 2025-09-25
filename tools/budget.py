# Importing Required Packagaes
from langchain import OpenAI
from prompts.templates import BUDGET_PROMPT
import json

# Create class for BudgeTool
class BudgetTool:
    
    # Define function to Intializing the self parameters
    def __init__(self, llm):
        self.llm = llm

    # Function to Estimate the Budget of the Trip
    def estimate_budget(self, trip_summary: str) -> dict:
        prompt = BUDGET_PROMPT.format(trip_summary=trip_summary)
        resp = self.llm.call_as_llm(prompt)
        try:
            return json.loads(resp)
        except Exception:
            return {"raw": resp}