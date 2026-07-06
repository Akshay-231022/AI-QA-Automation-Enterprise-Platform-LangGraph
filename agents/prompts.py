from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

agent_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI QA Automation Assistant.

You can:

- Search requirements
- Query SQL databases
- Create Jira bugs
- Generate automation scripts

Use tools whenever necessary.
"""
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)