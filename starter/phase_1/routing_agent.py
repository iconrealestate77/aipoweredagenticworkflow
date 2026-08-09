from dotenv import load_dotenv
import os
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent

# Load OpenAI API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

# Instantiate three specialized knowledge agents
texas_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key, persona,
    "You know everything about Texas history and geography."
)

europe_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key, persona,
    "You know everything about European history and geography."
)

math_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key, persona,
    "You are great at math. Explain your work step by step and give the final numeric answer."
)


# Define a function/lambda for each agent to be called when it's routed to
def texas_agent_func(prompt):
    return texas_agent.respond(prompt)


def europe_agent_func(prompt):
    return europe_agent.respond(prompt)


def math_agent_func(prompt):
    return math_agent.respond(prompt)


# Assign agents (with descriptions and callables) to the router
agents = [
    {
        "name": "Texas Knowledge Agent",
        "description": "Answers questions about the history, geography, and culture of Texas.",
        "func": texas_agent_func
    },
    {
        "name": "Europe Knowledge Agent",
        "description": "Answers questions about the history, geography, and culture of Europe.",
        "func": europe_agent_func
    },
    {
        "name": "Math Agent",
        "description": "Solves math problems and answers questions involving numbers and calculations.",
        "func": math_agent_func
    }
]

routing_agent = RoutingAgent(openai_api_key, agents)

# Test routing with the required prompts
test_prompts = [
    "Tell me about the history of Rome, Texas",
    "Tell me about the history of Rome, Italy",
    "One story takes 2 days, and there are 20 stories"
]

for prompt in test_prompts:
    print(f"\nPrompt: {prompt}")
    response = routing_agent.route(prompt)
    print(f"Response: {response}")
