# Importing Required Packages
from langchain import OpenAI
from prompts.templates import ACTIVITIES_PROMPT
import json

# Create class for finding the Activities
class ActivitiesTool:
    
    # Function to Initialize the 
    def __init__(self, llm):
        self.llm = llm

    # Function to Recommend the Activities
    def recommend(self, trip_summary: str) -> dict:
        prompt = ACTIVITIES_PROMPT.format(trip_summary=trip_summary)
        resp = self.llm.call_as_llm(prompt)
        try:
            return json.loads(resp)
        except Exception:
            return {"raw": resp}