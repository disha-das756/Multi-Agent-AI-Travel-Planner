from memory.trip_memory import save_trip_memory, get_similar_trips

def memory_agent(state):
    # Retrieve similar past trips
    similar_trips = get_similar_trips(
        state["destination"],
        state["interests"]
    )

    if similar_trips:
        state["personalized_suggestions"] = similar_trips
    else:
        state["personalized_suggestions"] = "No past trips found."

    # Save current trip
    save_trip_memory(state)

    return state