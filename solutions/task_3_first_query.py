#!/usr/bin/env python3
"""
Task 3: Execute First Query
Make your first call to Claude using the query() function.
"""

from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio
import os

# Configure options
options = ClaudeAgentOptions(
    env={
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        "ANTHROPIC_BASE_URL": os.getenv("ANTHROPIC_BASE_URL"),
    },
    model="claude-sonnet-4-20250514",
    allowed_tools=["Bash"],
    permission_mode="acceptEdits",
)

async def main():
    """Execute first query to Claude"""

    # SOLUTION: Complete the prompt
    prompt = "Hello Claude, please introduce yourself and explain what you can do with AWS"

    print("Executing first query to Claude...")
    print(f"Prompt: {prompt}\n")

    # SOLUTION: Use async for loop to iterate over query() results
    async for message in query(prompt=prompt, options=options):
        print(message)

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task3_first_query_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
