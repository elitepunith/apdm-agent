import os
import asyncio
from dotenv import load_dotenv

from google.adk.runners import InMemoryRunner
from agent import coordinator_agent

load_dotenv()

async def main():
    print("🚀 APDM Agent Ready!")
    print("Type 'exit' to quit.\n")

    runner = InMemoryRunner(agent=coordinator_agent)

    while True:
        msg = input("You: ").strip()
        if msg.lower() in ["exit", "quit"]:
            break

        result = await runner.run_debug(msg)

        responses = []

        for e in result:
            if hasattr(e, "content") and hasattr(e.content, "text"):
                txt = e.content.text
                if txt.strip():  # Only keep non-empty responses
                    responses.append(txt)

        if responses:
            print("\nAPDM >", responses[-1], "\n")
        else:
            pass  # Do nothing — no more "[No response]"

if __name__ == "__main__":
    asyncio.run(main())
