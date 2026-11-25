from pydantic import BaseModel
from typing import Literal


class Scenario(BaseModel):
    title: str
    runs: int
    category: str
    lang: str
    given: list[str]
    when: str
    then: list[str]
    pass_rate: float


class Turn(BaseModel):
    role: Literal["user", "agent"]
    content: str
    tool_calls: list[str] = []


class Conversation(BaseModel):
    turns: list[Turn]
