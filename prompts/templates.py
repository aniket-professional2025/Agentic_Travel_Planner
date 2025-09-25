# Define the Prompt for the Itinerary Services
ITINERARY_PROMPT = """
You are a travel assistant. Create a concise, day-by-day itinerary for the following trip request.

User request:
{user_request}

Constraints:
- Respond **only** with a valid JSON object.
- The entire JSON object **must be wrapped in ```json ... ``` fences**.
- The JSON object must contain the following top-level keys: **title**, **summary**, **days**, **budget_estimate**, and **recommended_pace**.
- The value for **days** must be a list of day objects.
- Each day object in the list must contain the keys: **day**, **date**, **morning**, **afternoon**, **evening**, and **notes**.
- The **morning**, **afternoon**, and **evening** keys must each contain a nested object with the keys: **activity** and **description**.
- Do not include any additional text or explanation outside of the JSON fences.

Example of the required JSON structure:
```json
{
  "title": "Your Trip Title",
  "summary": "A brief summary of the trip.",
  "days": [
    {
      "day": 1,
      "date": "Month Day",
      "morning": {
        "activity": "Activity name",
        "description": "Short description of the activity."
      },
      "afternoon": {
        "activity": "Activity name",
        "description": "Short description of the activity."
      },
      "evening": {
        "activity": "Activity name",
        "description": "Short description of the activity."
      },
      "notes": "Any extra notes for the day."
    }
  ],
  "budget_estimate": "Estimated budget.",
  "recommended_pace": "Suggested pace for the trip."
}
"""

# Define the Prompt for Budget Services
BUDGET_PROMPT = """
You are a travel finance assistant. Given trip details:

{trip_summary}

Estimate a simple budget broken down into: flights, accommodation (per night), food (per day), transportation (per day), activities, and contingency.
Output as a single JSON object. The main object should have a key called **trip_budget** which is another JSON object. Inside **trip_budget**, all budget categories **must** be present, each with an **estimate** and **currency** key. Additionally, **total_estimate** must be included with an **estimate** and **currency** key.
"""

# Define the Prompt for Packing Assistanc
PACKING_PROMPT = """
You are a helpful packing assistant. Given the destination, month/date, length of trip, traveler profile (adult, children), and 
planned activities, produce a categorized packing list (clothing, toiletries, electronics, documents, extras) with quantities.
Input:

{trip_summary}

Output:
JSON object with keys: clothing, toiletries, electronics, documents, extras
"""

# Define the Prompt for Activities
ACTIVITIES_PROMPT = """
Recommend top 6 activities and 4 restaurants/cafes for the destination based on traveler preferences (culture, adventure, food, 
family-friendly).
For each **activity**, you **must** provide a **name**, a **description** (1-2 sentences), and **time_needed**.
For each **restaurant/cafe**, you **must** provide a **name**, a **description** (1-2 sentences), and an **average_cost**.
Input:

{trip_summary}

Output: JSON object with two keys: "activities" (a list of objects) and "restaurants" (a list of objects).
"""