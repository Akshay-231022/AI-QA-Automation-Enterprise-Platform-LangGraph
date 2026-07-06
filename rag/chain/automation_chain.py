from config import llm
from prompts.automation_prompt import automation_prompt

automation_chain = (
    automation_prompt
    |
    llm
)