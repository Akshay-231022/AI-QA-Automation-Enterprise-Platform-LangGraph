from config import llm

from models.test_case import TestSuite

from prompts.test_case_prompt import test_case_prompt

structured_llm = llm.with_structured_output(
    TestSuite
)

test_case_chain = (
    test_case_prompt
    |
    structured_llm
)