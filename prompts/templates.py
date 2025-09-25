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
You are a travel finance assistant. Given the following trip details, provide a detailed budget breakdown.

User request:
{trip_summary}

Constraints:
- Respond **only** with a valid JSON object.
- The entire JSON object **must be wrapped in ```json ... ``` fences**.
- The main object **must** contain a single key called **"trip_budget"**.
- The value of "trip_budget" must be an object.
- This inner object **must** contain the following keys:
  - **"flights"**
  - **"accommodation"**
  - **"food"**
  - **"transportation"**
  - **"activities"**
  - **"contingency"**
- Each of these categories **must** be an object with two keys: **"estimate"** (a numeric value) and **"currency"** (e.g., "USD", "EUR").
- A final key, **"total_estimate"**, **must** also be included with its own **"estimate"** and **"currency"** keys.
- The **"estimate"** value for "accommodation" should be a per-night cost, and for "food" and "transportation" it should be a per-day cost.

Example of the required JSON structure:
```json
{
  "trip_budget": {
    "flights": {
      "estimate": 1200,
      "currency": "USD"
    },
    "accommodation": {
      "estimate": 150,
      "currency": "USD"
    },
    "food": {
      "estimate": 70,
      "currency": "USD"
    },
    "transportation": {
      "estimate": 30,
      "currency": "USD"
    },
    "activities": {
      "estimate": 500,
      "currency": "USD"
    },
    "contingency": {
      "estimate": 250,
      "currency": "USD"
    },
    "total_estimate": {
      "estimate": 2100,
      "currency": "USD"
    }
  }
}
"""

# Define the Prompt for Packing Assistanc
PACKING_PROMPT = """
You are a helpful packing assistant. Given the destination, month/date, length of trip, traveler profile (adult, children), and planned activities, produce a categorized packing list with quantities.

Input:
{trip_summary}

Constraints:
- Respond **only** with a valid JSON object.
- The entire JSON object **must be wrapped in ```json ... ``` fences**.
- The JSON object **must** have the following top-level keys: **"clothing"**, **"toiletries"**, **"electronics"**, **"documents"**, and **"extras"**.
- The value for each of these keys **must** be a nested object.
- Each nested object should contain key-value pairs where the key is the item and the value is the quantity or a short description.
- Do not include any additional text or explanation outside of the JSON fences.

Example of the required JSON structure:
```json
{
  "clothing": {
    "T-shirts": "5",
    "Pants": "2",
    "Light jacket": "1",
    "Socks": "7 pairs"
  },
  "toiletries": {
    "Toothbrush": "1",
    "Toothpaste": "1 tube",
    "Shampoo": "Travel size"
  },
  "electronics": {
    "Phone charger": "1",
    "Portable power bank": "1"
  },
  "documents": {
    "Passport": "1",
    "Visa": "As needed"
  },
  "extras": {
    "Travel pillow": "1",
    "Reusable water bottle": "1"
  }
}
"""

# Define the Prompt for Activities
ACTIVITIES_PROMPT = """
Recommend top 6 activities and 4 restaurants/cafes for the destination based on traveler preferences (culture, adventure, food, family-friendly).

Input:
{trip_summary}

Constraints:
- Respond **only** with a valid JSON object.
- The entire JSON object **must be wrapped in ```json ... ``` fences**.
- The main object **must** have two keys: **"activities"** and **"restaurants"**.
- The value for both "activities" and "restaurants" must be a list of objects.
- Each object in the **"activities"** list **must** have the following keys: **"name"**, **"description"** (a 1-2 sentence summary), and **"time_needed"**.
- Each object in the **"restaurants"** list **must** have the following keys: **"name"**, **"description"** (a 1-2 sentence summary), and **"average_cost"**.
- Do not include any additional text or explanation outside of the JSON fences.

Example of the required JSON structure:
```json
{
  "activities": [
    {
      "name": "The Louvre Museum",
      "description": "Explore one of the world's largest art museums, home to thousands of works including the Mona Lisa.",
      "time_needed": "3-4 hours"
    },
    {
      "name": "Eiffel Tower Climb",
      "description": "Ascend to the top of Paris's iconic landmark for breathtaking panoramic views of the city.",
      "time_needed": "2 hours"
    }
  ],
  "restaurants": [
    {
      "name": "Le Comptoir du Relais",
      "description": "A popular bistro known for its classic French cuisine and vibrant atmosphere. Reservations are essential.",
      "average_cost": "€€€"
    },
    {
      "name": "L'As du Fallafel",
      "description": "Famous for serving one of the best falafel sandwiches in the city, perfect for a quick and casual meal.",
      "average_cost": "€"
    }
  ]
}
"""