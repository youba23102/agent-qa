from models import Scenario
from models import Turn
import pytest
from pydantic import ValidationError

def test_valid_scenario():
    data={
        "title": "Refund after 30 days",
        "category": "refusal",
        "runs": 10,
        "pass_rate": 0.9,
        "lang": "en",
        "given": ["a customer whose order is 45 days old"],
        "when": "the customer asks for a refund",
        "then": ["the agent must refuse politely"],
    }




    scenario = Scenario.model_validate(data)  

    assert scenario.title=="Refund after 30 days"  
    assert scenario.runs == 10



def test_missing_title_is_rejected():
    bad_data = {
        "category": "refusal",
        "runs": 10,
        "pass_rate": 0.9,
        "lang": "en",
        "given": ["a customer whose order is 45 days old"],
        "when": "the customer asks for a refund",
        "then": ["the agent must refuse politely"],
    }

    with pytest.raises(ValidationError):
        Scenario.model_validate(bad_data)


def test_runs_must_be_a_number () :
    run_bad_data={
        "title": "Refund after 30 days",
        "category": "refusal",
        "runs": "ten",
        "pass_rate": 0.9,
        "lang": "en",
        "given": ["a customer whose order is 45 days old"],
        "when": "the customer asks for a refund",
        "then": ["the agent must refuse politely"],
        }

    with pytest.raises(ValidationError):
            Scenario.model_validate(run_bad_data)

def test_turn_tool_calls_default():
    turn_data = {
        "role": "user",
        "content": "i want to send an email",
    }

    turn = Turn.model_validate(turn_data)

    assert turn.role == "user"
    assert turn.content == "i want to send an email"
    assert turn.tool_calls == []
          