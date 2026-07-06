from langchain_core.tools import tool



@tool
def create_bug(summary: str, description: str) -> str:
    """
    Creates a Jira bug.
    """

    print("Calling Jira API...")

    return f"Bug created successfully: {summary}"