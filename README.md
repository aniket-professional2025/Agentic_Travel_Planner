# Agentic_Travel_Planner
This project deals with how we can create an agent using openai models that can analyse a human prompt on what they want and then plan the steps like Food, Activity, Budget, Packing etc. We use Streamlit as the frontend

### Project Overview 🧳
The AI Travel Planner is an intelligent agent designed to help users plan their trips. By taking a simple request like "5 days in Lisbon, 2 adults, food + culture, mid-budget," the agent generates a comprehensive trip plan, including a day-by-day itinerary, activity and restaurant recommendations, a budget estimate, and a packing list. This project leverages large language models (LLMs) to automate the trip planning process, providing users with a tailored and well-structured travel guide.

### Project Structure 🗺️
The project is organized into logical directories to separate concerns and ensure maintainability.
* main.py: The command-line interface (CLI) entry point for the application.
* agent.py: Contains the TravelAgent class and a simple LLM wrapper that orchestrates the entire trip planning process.
* memory_store.py: Handles local session persistence, saving generated trip plans to a file for later use.
* prompts/: Stores the prompt templates used by the agent to guide the LLM's output for specific tasks.
* tools/: A collection of specialized modules (e.g., itinerary_tool.py, budget_tool.py) that represent the agent's core capabilities.
* examples/: Contains examples of how to run the agent and transcripts of a successful run.

### How to Get Help and Contribute 🤝
If you encounter an issue, have questions, or want to contribute to this project, here's how you can get help:
* Report an Issue: If you find a bug or a problem with the generated output, please open an issue on the project's GitHub page. Provide a detailed description, including the user request that caused the issue and any error messages you received.
* Ask a Question: For general inquiries about the code, the LLM integration, or best practices, feel free to start a discussion.
* Contribute: We welcome contributions! Whether it's fixing a bug, improving the prompts, or adding new features (like hotel recommendations or weather integration), your help is appreciated. Please follow the standard pull request process.
