# A minimal LangGraph wiring that demonstrates how to split planning into nodes.
# This file is intentionally small and optional — the agent in `agent.py` works without it.

# Importing Required Packages
from langgraph import Graph, Node
from agent import TravelAgent

# Define the function to define the graph
def build_graph():
    g = Graph(name = "travel_planner")
    agent = TravelAgent()

    def plan_node(context):
        req = context.get("user_request")
        result = agent.plan_trip(req)
        context["result"] = result
        return context

    plan = Node(run=plan_node, name="plan_trip")
    g.add_node(plan)
    return g

# The main Inference block
if __name__ == "__main__":
    G = build_graph()
    ctx = {"user_request": "3-day food and culture trip to Kyoto for two adults in Oct, mid budget"}
    out = G.run(ctx)
    print(out.get("result"))