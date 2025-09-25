# Importing Required Libraries
import streamlit as st
import json
import re
import time
from pathlib import Path
from agent import TravelAgent
from memory_store import MemoryStore

# The Memory file path
MEM_FILE = Path(".travel_memory.json")

# Function to Extract JSON from raw strings
def extract_json(raw_text: str):
    """Extract and parse JSON from a raw string with ```json fences."""
    if not raw_text:
        return None
    match = re.search(r"```json(.*?)```", raw_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except Exception:
            return None
    try:
        return json.loads(raw_text)
    except Exception:
        return None

# Load the latest session
def load_latest_session():
    if not MEM_FILE.exists():
        return None
    data = json.loads(MEM_FILE.read_text())
    sessions = data.get("sessions", [])
    return sessions[-1] if sessions else None


# ------------------- Streamlit UI -------------------

st.set_page_config(page_title="AI Travel Planner", layout="wide")
st.title("🧳 AI Travel Planner")

# User input
user_prompt = st.text_input(
    "Enter your trip details:",
    placeholder="5 days in Lisbon, 2 adults, food + culture, mid-budget",
)

# Initialize logs
if "logs" not in st.session_state:
    st.session_state.logs = []

# Plan Trip button
if st.button("✨ Plan Trip"):
    if not user_prompt.strip():
        st.warning("Please enter your trip details first!")
    else:
        st.session_state.logs = []  # reset logs
        log_area = st.container()

        # Simulated step-by-step logging
        steps = [
            "📖 Reading the User Idea...",
            "⛓️‍💥 Breaking the User prompt into multiple small chinks..."
            "📌 Analyzing your request...",
            "🗺️ Designing your day-by-day itinerary...",
            "🎯 Finding must-do activities and restaurants...",
            "💰 Estimating your trip budget...",
            "🎒 Preparing a packing list...",
            "✅ Trip plan ready!",
        ]

        # Run the agent
        agent = TravelAgent()
        mem = MemoryStore()

        for idx, step in enumerate(steps):
            st.session_state.logs.append(step)
            with log_area:
                for log in st.session_state.logs:
                    st.write(log)
            time.sleep(3)

            # At the right step, actually run the agent
            if idx == 0:  # after first log
                result = agent.plan_trip(user_prompt)
                mem.save_session({"request": user_prompt, "result": result})

        # Load the freshly saved session
        session = load_latest_session()
        if not session:
            st.error("Trip planning failed. No session saved.")
        else:
            result = session["result"]

            # ---- Itinerary ----
            st.header("🗺️ Itinerary")
            itinerary_json = extract_json(result["itinerary"].get("raw"))
            if itinerary_json:
                st.subheader(itinerary_json.get("title", "Trip Itinerary"))
                st.caption(itinerary_json.get("summary", ""))
                for day in itinerary_json.get("days", []):
                    with st.expander(f"Day {day['day']} - {day.get('date','')}"):
                        # Use .get() with an empty string as a default value
                        st.markdown(f"**Morning:** {day['morning'].get('activity', '')} — {day['morning'].get('description', '')}")
                        st.markdown(f"**Afternoon:** {day['afternoon'].get('activity', '')} — {day['afternoon'].get('description', '')}")
                        st.markdown(f"**Evening:** {day['evening'].get('activity', '')} — {day['evening'].get('description', '')}")
                        st.info(day.get("notes", ""))
                st.success(f"Budget Estimate: {itinerary_json.get('budget_estimate','')}")
                st.info(f"Recommended Pace: {itinerary_json.get('recommended_pace','')}")

            # ---- Activities ----
            st.header("🎯 Activities & Dining")
            activities_json = extract_json(result["activities"].get("raw"))
            if activities_json:
                st.subheader("Activities")
                for act in activities_json.get("activities", []):
                    # Using .get() to safely access keys
                    st.markdown(
                        f"- **{act.get('name', '')}** ({act.get('time_needed', '')}): {act.get('description', '')}")
                st.subheader("Restaurants")
                for rest in activities_json.get("restaurants", []):
                    # Using .get() to safely access keys
                    st.markdown(
                        f"- **{rest.get('name', '')}** ({rest.get('average_cost', '')}): {rest.get('description', '')}")

            # ---- Budget ----
            st.header("💰 Budget")
            budget_json = extract_json(result["budget"].get("raw"))
            if budget_json:
                trip_budget = budget_json.get("trip_budget", {})
                for key, val in trip_budget.items():
                    if isinstance(val, dict):
                        st.markdown(
                            f"- **{key.title()}**: {val.get('estimate', val.get('total',''))} {val.get('currency','')}")
                st.success(
                    f"Total Estimate: {trip_budget.get('total_estimate', {}).get('estimate', '')} "
                    f"{trip_budget.get('total_estimate', {}).get('currency', '')}"
                )

            # ---- Packing ----
            st.header("🎒 Packing List")
            packing_json = extract_json(result["packing"].get("raw"))
            if packing_json:
                for section, items in packing_json.items():
                    with st.expander(section.title()):
                        for k, v in items.items():
                            st.markdown(f"- {k.replace('_',' ').title()}: {v}")