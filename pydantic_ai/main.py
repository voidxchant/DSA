import os
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

# Step 1: Define a structured output model
class Response(BaseModel):
    answer: str

# Step 2: Load your API key
os.environ.setdefault("GEMINI_API_KEY", "YOUR_GEMINI_KEY")

# Step 3: Initialize GeminiModel + Agent
model = GeminiModel("gemini-2.5-flash", provider="google-gla")
agent = Agent(model, output_type=Response, system_prompt="You are a helpful assistant.")

# Step 4: Use string prompt directly
if __name__ == "__main__":
    result = agent.run_sync("how ti make a python coding agent using pydantic-ai?")
    print("Answer:", result.output.answer)
    print("Usage:", result.usage())
