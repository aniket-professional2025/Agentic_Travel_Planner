# Importing Required Packages
from langchain import OpenAI
from prompts.templates import PACKING_PROMPT
import json

# Create class for filling up the Packing details
class PackingTool:
    
    # Define function to Initialize the 
    def __init__(self, llm):
        self.llm = llm

    # Define function to create the packing list
    def packing_list(self, trip_summary: str) -> dict:
        prompt = PACKING_PROMPT.format(trip_summary=trip_summary)
        resp = self.llm.call_as_llm(prompt)
        try:
            return json.loads(resp)
        except Exception:
            return {"raw": resp}