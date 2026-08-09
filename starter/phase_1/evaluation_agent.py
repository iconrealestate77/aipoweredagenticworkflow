from dotenv import load_dotenv
import os
from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent

# Load OpenAI API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Instantiate the worker agent (deliberately given wrong knowledge, per spec)
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Instantiate the evaluation agent
eval_persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a full sentence."

evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=eval_persona,
    evaluation_criteria=evaluation_criteria,
    worker_agent=knowledge_agent,
    max_interactions=10
)

# Evaluate the prompt and print the result
prompt = "What is the capital of France?"
evaluation_result = evaluation_agent.evaluate(prompt)

print("\n=== Final Evaluation Result ===")
print(f"Final Response: {evaluation_result['final_response']}")
print(f"Evaluation: {evaluation_result['evaluation']}")
print(f"Iterations Used: {evaluation_result['iterations']}")
