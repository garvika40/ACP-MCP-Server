import asyncio
from acp_sdk.client import Client


async def list_agents():
    async with Client(base_url="http://localhost:8000") as client:
        async for agent in client.agents():
            print(agent)


if __name__ == "__main__":
    asyncio.run(list_agents())
