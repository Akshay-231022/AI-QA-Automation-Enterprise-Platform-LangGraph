from pydantic import BaseModel


class TestCase(BaseModel):

    test_case_id: str

    title: str

    precondition: str

    steps: list[str]

    expected_result: str

    priority: str