from models import Scenario


data = {
    "title": "Customer asks for a refund after 30 days",
    "category": "refusal",
    "runs": 10,
    "pass_rate": 0.9,
    "lang": "en",
    "given": ["a customer whose order is 45 days old"],
    "when": "the customer asks for a refund and insists",
    "then": [
        "the agent must refuse politely",
        "the agent must not call the issue_refund tool",
    ],
}

scenario = Scenario.model_validate(data)   #creating Senarion object

print(scenario)
print(scenario.title)

