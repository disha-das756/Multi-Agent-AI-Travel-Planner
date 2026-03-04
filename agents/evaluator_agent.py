from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

def evaluator_agent(state):
    template = """
You are a travel plan evaluator.

Evaluate this travel plan:

{itinerary}

Return:

Quality Score: X/10
Coverage Score: X/10
Practicality Score: X/10

Strengths:
- bullet points

Weaknesses:
- bullet points

Improvements:
- bullet points
"""

    prompt = PromptTemplate(
        input_variables=["itinerary"],
        template=template
    )

    response = llm.invoke(
        prompt.format(itinerary=state["itinerary"])
    )

    state["evaluation_report"] = response.content
    return state