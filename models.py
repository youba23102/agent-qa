from pydantic import BaseModel

class Scenario(BaseModel):
    title: str
    runs: int
    category: str
    lang: str
    given: list[str]
    when: str
    then: list[str]
    pass_rate: float