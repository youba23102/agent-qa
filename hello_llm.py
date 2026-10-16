from dotenv import load_dotenv
from litellm import completion


load_dotenv()


messages = [
    {"role": "user", "content": "Say hello in one short sentence."}
]




response = completion(
    model = "anthropic/claude-haiku-4-5",
    messages = messages
)


print(response.choices[0].message.content)




