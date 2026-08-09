from dotenv import load_dotenv
import os
from workflow_agents.base_agents import DirectPromptAgent

# Load OpenAI API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Instantiate the DirectPromptAgent
direct_agent = DirectPromptAgent(openai_api_key)

# Send a prompt to the agent
prompt = "What is the Capital of France?"
direct_agent_response = direct_agent.respond(prompt)

# Print the response
print(f"Prompt: {prompt}")
print(f"Response: {direct_agent_response}")

# Explain the source of knowledge used to answer the prompt
print(
    "\nKnowledge source: This agent has no persona, external knowledge, or retrieval "
    "mechanism. Its answer comes purely from the general knowledge gpt-3.5-turbo learned "
    "during training, since no system prompt or additional context was provided."
)
