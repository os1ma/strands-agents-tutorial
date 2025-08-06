from dotenv import load_dotenv
from strands import Agent

load_dotenv()

# Create an agent with default settings
agent = Agent()

# Ask the agent a question
agent("Tell me about agentic AI")
