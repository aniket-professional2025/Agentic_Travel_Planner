# Importing Required Packages
import os
from dotenv import load_dotenv
from rich.console import Console
from agent import TravelAgent
from memory_store import MemoryStore

# Loading the Environmental Variables
load_dotenv()
console = Console()

# Define function to make the process interactive
def interactive():
    console.rule("Travel Planner Agent")
    console.print("Enter a short description of your trip (destination, dates, travellers, preferences, budget):")
    user_request = console.input("[bold green]Trip> ")

    agent = TravelAgent()
    console.print("\nPlanning trip — this may take a moment as the model reasons...\n")
    result = agent.plan_trip(user_request)

    console.print("\n[bold underline]Itinerary:\\n")
    console.print(result.get("itinerary"))

    console.print("\n[bold underline]Activities:\\n")
    console.print(result.get("activities"))

    console.print("\n[bold underline]Budget Estimation:\\n")
    console.print(result.get("budget"))

    console.print("\n[bold underline]Packing List:\\n")
    console.print(result.get("packing"))

    # Save to memory
    mem = MemoryStore()
    mem.save_session({"request": user_request, "result": result})
    console.print("\nSaved session to memory (.travel_memory.json)\n")


# Inference on the interavtive function
if __name__ == "__main__":
    interactive()