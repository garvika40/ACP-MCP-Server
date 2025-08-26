from acp_sdk.models import Message, MessagePart
from acp_sdk.server import Server
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

server = Server()

# Define LLM
llm = LLM(model="gemini-2.5-pro", max_token=3000)
# ------------------------------
# Second Agent: Recipe Suggester
# ------------------------------
@server.agent()
async def recipe_suggester(input):
    """
    Agent that suggests 2-3 recipes based on the available ingredients
    provided in the input.
    """
    ingredients = input[0].parts[0].content

    agent = CodeAgent(
        tools=[],   # no external tool, just reasoning with the LLM
        model=model
    )

    prompt = f"Suggest 2-3 easy recipes that can be made using these ingredients: {ingredients}."
    response = agent.run(prompt)
    yield Message(parts=[MessagePart(content=str(response))])


# ------------------------------
# Run the Server
# ------------------------------
if __name__ == "__main__":
    server.run(port=8001)