from langchain_core.prompts import ChatPromptTemplate

test_case_prompt = ChatPromptTemplate.from_template(
"""
You are a Senior QA Automation Engineer.

Using ONLY the provided requirement, generate comprehensive test cases.

Requirement:

{context}

Generate:

• Positive Test Cases

• Negative Test Cases

• Boundary Test Cases

• Validation Test Cases

For each test case provide

Test Case ID

Title

Precondition

Steps

Expected Result

Priority

Do not invent functionality not present in the requirement.
"""
)