def qa_planner_agent(state):

    print("Planning QA workflow...")

    state["plan"] = [

        "Generate Test Cases",

        "Generate Automation",

        "Execute Tests"

    ]

    return state
