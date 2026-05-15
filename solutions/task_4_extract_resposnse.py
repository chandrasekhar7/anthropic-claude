#!/usr/bin/env python3
"""
Task 4: Extract Response Content
Learn how to extract text from Claude's responses.
"""

from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio
import os

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
    """Query Claude and extract response text"""

    prompt = "Explain what Claude Agent SDK is in 2 sentences"

    print("Querying Claude...\n")

    # Iterate over messages from Claude
    async for message in query(prompt=prompt, options=options):
        # Check if message is an AssistantMessage (has 'content' attribute)
        if hasattr(message, 'content'):
            # Extract text from content blocks
            # AssistantMessage has a 'content' attribute which is a list of blocks
            # Each TextBlock has a 'text' attribute
            for block in message.content:
                if hasattr(block, 'text'):
                    response_text = block.text  # SOLUTION: Get block.text
                    print(f"Claude's Response: {response_text}")

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task4_extract_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
