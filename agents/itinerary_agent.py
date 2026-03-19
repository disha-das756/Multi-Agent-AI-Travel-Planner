import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Get the absolute path to the prompts directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_PATH = os.path.join(BASE_DIR, "prompts", "itinerary_prompt.txt")

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

def itinerary_agent(state):
    with open(PROMPT_PATH, encoding="utf-8") as f:
        template = f.read()

    # Add popular_places to the template if it's not already there
    if "{popular_places}" not in template:
        template = template.replace("Interests: {interests}", "Interests: {interests}\nPopular Places to Consider: {popular_places}")

    prompt = PromptTemplate(
        input_variables=[
            "source",
            "destination",
            "days",
            "budget",
            "interests",
            "travel_style",
            "popular_places"
        ],
        template=template
    )

    response = llm.invoke(
        prompt.format(
            source=state["source"],
            destination=state["destination"],
            days=state["days"],
            budget=state["budget"],
            interests=", ".join(state["interests"]),
            travel_style=state["travel_style"],
            popular_places=state.get("popular_places", "Not search results found.")
        )
    )

    state["itinerary"] = response.content
    return state