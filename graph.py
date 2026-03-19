from typing import TypedDict
from langgraph.graph import StateGraph, END

# Import agents
from agents.places_agent import places_agent
from agents.itinerary_agent import itinerary_agent
from agents.budget_agent import budget_agent
from agents.evaluator_agent import evaluator_agent


# -----------------------------
# STATE DEFINITION
# -----------------------------

class TripState(TypedDict):
    source: str
    destination: str
    days: int
    budget: str
    interests: list
    travel_style: str

    itinerary: str
    budget_estimate: str
    evaluation_report: str
    popular_places: str


# -----------------------------
# BUILD GRAPH
# -----------------------------

graph = StateGraph(TripState)

graph.add_node("places", places_agent)
graph.add_node("itinerary", itinerary_agent)
graph.add_node("budget", budget_agent)
graph.add_node("evaluator", evaluator_agent)


graph.set_entry_point("places")
graph.add_edge("places", "itinerary")
graph.add_edge("itinerary", "budget")
graph.add_edge("budget", "evaluator")
graph.add_edge("evaluator", END)

app_graph = graph.compile()
