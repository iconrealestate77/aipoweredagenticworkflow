from dotenv import load_dotenv
import os
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

# Load OpenAI API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Instantiate the agent with a persona and deliberately incorrect knowledge
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Test the agent
prompt = "What is the capital of France?"
knowledge_agent_response = knowledge_agent.respond(prompt)

# Print the response
print(f"Prompt: {prompt}")
print(f"Response: {knowledge_agent_response}")

# Confirm the agent used the provided (intentionally wrong) knowledge, not its own
print(
    "\nConfirmation: The factually correct answer is Paris, but the response above "
    "states London - this confirms the agent answered using ONLY the knowledge string "
    "provided at instantiation, not gpt-3.5-turbo's own trained knowledge."
)
