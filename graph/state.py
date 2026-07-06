from typing import TypedDict


class QAState(TypedDict):

    requirement: str

    test_cases: list

    approved: bool

    playwright_code: str

    execution_result: str

    jira_ticket: str