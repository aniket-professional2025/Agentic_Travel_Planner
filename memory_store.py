# Importing Required Packages
import json
from pathlib import Path

# Defining the Memory File Path
MEM_FILE = Path(".travel_memory.json")

# Creating a class MemoryStore To Store the Memory
class MemoryStore:
    
    # Defining function to initialize the self parameters
    def __init__(self):
        if MEM_FILE.exists():
            self.data = json.loads(MEM_FILE.read_text())
        else:
            self.data = {"sessions": []}

    # Define function to save the sessions
    def save_session(self, session: dict):
        self.data["sessions"].append(session)
        MEM_FILE.write_text(json.dumps(self.data, indent=2))

    # Define function to list all sessions
    def list_sessions(self):
        return self.data.get("sessions", [])