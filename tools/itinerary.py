# Importing Required Packages
from prompts.templates import ITINERARY_PROMPT
import json
import re

# Creating a class for the ItineraryTools
class ItineraryTool:

    # The Function to Initialize the self values
    def __init__(self, llm):
        self.llm = llm

    # Function to Create the Itinerary
    def create_itinerary(self, user_request: str) -> dict:
        prompt = ITINERARY_PROMPT.format(user_request=user_request)
        resp = self.llm.call_as_llm(prompt)
        
        # New: Extract the JSON content and strip whitespace
        match = re.search(r"```json(.*?)```", resp, re.DOTALL)
        if match:
            clean_resp = match.group(1).strip()
        else:
            clean_resp = resp.strip()

        # The model is asked to return JSON — be tolerant and try to parse.
        try:
            data = json.loads(resp)
        except Exception:
            # fallback: wrap the raw text in a field
            data = {"raw": resp}
        return data