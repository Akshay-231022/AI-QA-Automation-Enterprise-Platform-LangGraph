from langchain.agents import create_sql_agent

sql_agent = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="tool-calling",
    verbose=True
)