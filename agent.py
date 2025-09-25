# Importing Required Packages
import os
from tools.itinerary import ItineraryTool
from tools.budget import BudgetTool
from tools.packing import PackingTool
from tools.activities import ActivitiesTool
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Importing Environmental Variables
load_dotenv()

# SimpleLLMWrapper class Using Langchain ChatOpenAI
class SimpleLLMWrapper:

    # Define the function to Intialize the class parameters
    def __init__(self, model_name: str | None = None):
        model_name = model_name or os.environ.get("OPENAI_MODEL") or "gpt-4o-mini"
        key = os.environ.get("OPENAI_API_KEY")
        self.llm = ChatOpenAI(api_key = key, model = model_name)

    # Define the function to to call the llm
    def call_as_llm(self, prompt: str) -> str:
        resp = self.llm([HumanMessage(content=prompt)])
        return resp.content

# # Creating a class for the LLM wrapper
# class SimpleLLMWrapper:
    
#     # Define the function to Intialize the class parameters
#     def __init__(self, model_name: str | None = None):
#         model_name = model_name or os.environ.get("OPENAI_MODEL") or "gpt-4o-mini"
#         self.llm = OpenAI(model_name = model_name)

#     # Define the function to to call the llm
#     def call_as_llm(self, prompt: str) -> str:
#         # We ask langchain OpenAI wrapper to produce text and return it.
#         # resp = self.llm.generate([{"role": "user", "content": prompt}])
#         resp = self.llm.generate([prompt])  # just pass a list of strings
#         # pick the first generation
#         return resp.generations[0][0].text

# Creating the class for Travel agent
class TravelAgent:
    
    # Define the function to Initialize the class parameters
    def __init__(self, model_name: str | None = None):
        self.llm = SimpleLLMWrapper(model_name)
        self.itinerary = ItineraryTool(self.llm)
        self.budget = BudgetTool(self.llm)
        self.packing = PackingTool(self.llm)
        self.activities = ActivitiesTool(self.llm)

    # Define function to plan the trip
    def plan_trip(self, user_request: str) -> dict:
        # Create itinerary
        itinerary = self.itinerary.create_itinerary(user_request)
        # Create activities
        activities = self.activities.recommend(user_request)
        # Create budget
        budget = self.budget.estimate_budget(user_request)
        # Create packing list
        packing = self.packing.packing_list(user_request)

        # Storing the results into summary as below
        summary = {
            "user_request": user_request,
            "itinerary": itinerary,
            "activities": activities,
            "budget": budget,
            "packing": packing,
        }

        return summary