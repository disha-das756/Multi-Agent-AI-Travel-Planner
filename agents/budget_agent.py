import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate # PromptTemplate helps you create dynamic prompts.Instead of hard-coding text, you define placeholders ({destination}, {days}, etc.).

from dotenv import load_dotenv

load_dotenv()

# Get the absolute path to the prompts directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_PATH = os.path.join(BASE_DIR, "prompts", "budget_prompt.txt")


# Initialize the model
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile", 
    temperature=0
)




def budget_agent(state):
    with open(PROMPT_PATH, encoding="utf-8") as f:
        template = f.read()   # Reads the prompt text from an external file.


    prompt = PromptTemplate(
        input_variables=["source","destination","days","budget"],
        template=template
    )  


    response = llm.invoke(
        prompt.format(
            source=state["source"],
            destination = state["destination"],
            days=state["days"],
            budget=state["budget"]
        )
    )

    state["budget_estimate"] = response.content  # response.content contains the actual generated text from the model.
    return state  #Returns the modified state dictionary.Required for:LangGraph transitions.Multi-agent pipelines