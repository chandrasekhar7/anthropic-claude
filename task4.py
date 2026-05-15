#!/usr/bin/env python3
"""
Task 4: Extract Response Content
Learn how to extract text from Claude's responses.
"""

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock, ToolUseBlock, ResultMessage
import asyncio
import os

options = ClaudeAgentOptions(
    env={
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        "ANTHROPIC_BASE_URL": os.getenv("ANTHROPIC_BASE_URL"),
    },
    model="claude-sonnet-4-6",
    allowed_tools=["Bash"],
    permission_mode="acceptEdits",
)

async def main():
    """Query Claude and extract response text"""

    prompt = "Explain what Claude Agent SDK is in 2 sentences"

    print("Querying Claude...\n")

    # Iterate over messages from Claude
    async for message in query(prompt=prompt, options=options):
        # TODO: Check if message is an AssistantMessage
        # Hint: isinstance(message, AssistantMessage)
        if isinstance(message, ___):  # TODO: AssistantMessage
            # TODO: Extract text from content blocks
            # AssistantMessage has a 'content' attribute which is a list of blocks
            # Each TextBlock has a 'text' attribute
            for block in message.content:
                if isinstance(block, ___):  # TODO: TextBlock
                    response_text = ___  # TODO: block.text
                    print(f"Claude's Response: {response_text}")
                    print()
                elif isinstance(block, ToolUseBlock):
                    print(f"[Tool Used: {block.name}]")
                    print()
        elif isinstance(message, ResultMessage):
            print("\n" + "="*50)
            print("Execution Summary:")
            print("="*50)
            print(f"Duration: {message.duration_ms}ms")
            print(f"Cost: ${message.total_cost_usd:.6f}")
            print(f"Input tokens: {message.usage['input_tokens']}")
            print(f"Output tokens: {message.usage['output_tokens']}")
            print(f"Agent turns: {message.num_turns}")
            print("="*50)

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task4_extract_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
