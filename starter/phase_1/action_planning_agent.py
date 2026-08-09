from dotenv import load_dotenv
import os
from workflow_agents.base_agents import ActionPlanningAgent

# Load OpenAI API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Provide the agent with knowledge of how to make scrambled eggs
knowledge = (
    "Steps to prepare scrambled eggs: "
    "1. Crack the eggs into a bowl. "
    "2. Whisk the eggs together with a fork. "
    "3. Heat a pan on the stove over low-medium heat. "
    "4. Melt some butter in the pan. "
    "5. Pour the whisked eggs into the pan. "
    "6. Stir the eggs continuously while they cook. "
    "7. Remove the eggs from the pan once they are cooked to your liking. "
    "8. Season with salt and pepper and serve."
)

action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge)

# Test the agent
prompt = "One morning I wanted to have scrambled eggs"
steps = action_planning_agent.extract_steps_from_prompt(prompt)

print(f"Prompt: {prompt}")
print("Extracted Steps:")
for step in steps:
    print(f"- {step}")
