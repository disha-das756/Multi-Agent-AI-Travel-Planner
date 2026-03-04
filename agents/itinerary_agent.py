from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

def itinerary_agent(state):
    with open("prompts/itinerary_prompt.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=[
            "source",
            "destination",
            "days",
            "budget",
            "interests",
            "travel_style"
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
            travel_style=state["travel_style"]
        )
    )

    state["itinerary"] = response.content
    return state