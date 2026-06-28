import anthropic
from core.config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """
You are an AI Research Assistant.

Your job:
- Answer questions clearly and accurately
- Break explanations into structured key points
- Make complex topics easy to understand

Format:

Answer:
...

Key Points:
- ...
- ...
"""

def ask_llm(query: str):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return response.content[0].text