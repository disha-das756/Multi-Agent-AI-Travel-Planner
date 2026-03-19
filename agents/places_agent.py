from langchain_community.tools import DuckDuckGoSearchRun


search = DuckDuckGoSearchRun()


def places_agent(state):
    destination = state["destination"]

    query = f"Top tourist places to visit in {destination}"

    results = search.run(query)

    state["popular_places"] = results
    return state