
from langgraph.graph import StateGraph

from graph.state import QAState

builder = StateGraph(QAState)


builder.add_node(
    "generate_test_cases",
    generate_test_cases
)

builder.add_node(
    "human_review",
    human_review
)

builder.add_node(
    "generate_playwright",
    generate_playwright
)

builder.add_node(
    "generate_test_cases",
    generate_test_cases
)

builder.add_node(
    "human_review",
    human_review
)

builder.add_node(
    "generate_playwright",
    generate_playwright
)