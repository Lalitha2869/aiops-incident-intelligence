import json

from langgraph.graph import (
    StateGraph,
    END
)

from backend.state.incident_state import (
    IncidentState
)

from backend.agents.log_analyzer import (
    analyze_log
)

from backend.agents.retrieval_agent import (
    retrieve_similar_incidents
)

from backend.agents.rca_agent import (
    generate_rca
)

from backend.agents.recommendation_agent import (
    generate_recommendations
)

from backend.agents.validator_agent import (
    validate_incident
)


workflow = StateGraph(
    IncidentState
)


# -----------------------------
# Analyzer Node
# -----------------------------
def analyzer_node(state):

    print("Analyzer Started")

    result = analyze_log(
        state["logs"]
    )

    try:
        state["analysis"] = json.loads(
            result
        )
    except:
        state["analysis"] = result

    return state


# -----------------------------
# Retrieval Node
# -----------------------------
def retrieval_node(state):

    print("Retrieval Started")

    result = retrieve_similar_incidents(
        state["logs"]
    )

    state["retrieved_incidents"] = result

    return state


# -----------------------------
# RCA Node
# -----------------------------
def rca_node(state):

    print("RCA Started")

    historical_context = "\n".join(
        [str(item) for item in state["retrieved_incidents"]]
    )

    result = generate_rca(
        state["logs"],
        historical_context
    )

    state["rca"] = result

    return state


# -----------------------------
# Recommendation Node
# -----------------------------
def recommendation_node(state):

    print("Recommendation Started")

    result = generate_recommendations(
        state["rca"]["root_cause"]
    )

    state["recommendations"] = result

    return state


# -----------------------------
# Validator Node
# -----------------------------
def validator_node(state):

    print("Validator Started")

    recommendations_text = "\n".join(
        state["recommendations"]["recommendations"]
    )

    result = validate_incident(
        state["rca"]["root_cause"],
        recommendations_text
    )

    state["validation"] = result

    return state


# -----------------------------
# Graph Nodes
# -----------------------------
workflow.add_node(
    "analyzer",
    analyzer_node
)

workflow.add_node(
    "retrieval",
    retrieval_node
)

workflow.add_node(
    "rca",
    rca_node
)

workflow.add_node(
    "recommendation",
    recommendation_node
)

workflow.add_node(
    "validator",
    validator_node
)


# -----------------------------
# Flow
# -----------------------------
workflow.set_entry_point(
    "analyzer"
)

workflow.add_edge(
    "analyzer",
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "rca"
)

workflow.add_edge(
    "rca",
    "recommendation"
)

workflow.add_edge(
    "recommendation",
    "validator"
)

workflow.add_edge(
    "validator",
    END
)


# -----------------------------
# Compile Graph
# -----------------------------
graph = workflow.compile()