from langchain_core.prompts import ChatPromptTemplate

automation_prompt = ChatPromptTemplate.from_template(
"""
You are a Senior QA Automation Engineer.

Generate Playwright Python code for the following test case.

Test Case

{test_case}

Requirements:

- Use pytest
- Use Playwright
- Use explicit assertions
- Add comments
- Follow Page Object Model where appropriate
- Return only valid Python code
"""
)