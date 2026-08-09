from dotenv import load_dotenv
import os
from workflow_agents.base_agents import AugmentedPromptAgent

# Load OpenAI API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define a persona and instantiate the AugmentedPromptAgent
persona = "a helpful pirate captain who always speaks in pirate slang"
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

# Send a prompt to the agent
prompt = "What is the Capital of France?"
augmented_agent_response = augmented_agent.respond(prompt)

# Print the response
print(f"Prompt: {prompt}")
print(f"Response: {augmented_agent_response}")

# --- Explanatory comments ---
# Knowledge source: Like DirectPromptAgent, this agent has no external knowledge base -
# it still relies entirely on gpt-3.5-turbo's general training knowledge to answer
# factual questions like this one.
#
# Persona impact: The system prompt instructing the model to adopt the pirate captain
# persona (and forget any prior context) changed the STYLE and TONE of the response -
# pirate slang, phrasing, personality - while the underlying fact (Paris) stayed
# correct. The persona shapes *how* the answer is delivered, not *what* the model knows.
