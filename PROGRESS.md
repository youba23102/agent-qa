## Done
- Project folder qa_agent + virtual environment .venv
- Git initialized, .gitignore committed (ignores .venv and .env)
- LiteLLM installed
- .env with the Anthropic API key (never committed)
- hello_llm.py: first call to Claude Haiku through LiteLLM, working
- Pushed to GitHub: github.com/youba23102/agent-qa
- Pydantic concept + full Agent QA flow understood (Nov 3, Nov 10)
- Scenario validated with good data + bad data (missing title, runs="ten" → 2 errors caught)
- pytest: 3 tests on Scenario (1 positive, 2 negative) + mutation test



Step 2: data models in models.py
-designed the Scenario fields (name + type)

## Now
Now → Next: Turn and Conversation models

- Next: Turn and Conversation models

## Blockers / questions
- Re-test LiteLLM vs Adapter at step 5

## Key ideas
- LiteLLM = our agents think. Adapter = HTTP to their chatbot. Python loop in the middle.

## Sessions
- Oct 14, Oct 15, Oct 21, Oct 26, Nov 3, Nov 10, Nov 14 , Nov 16