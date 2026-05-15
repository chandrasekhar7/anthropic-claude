#!/usr/bin/env python3
"""
Task 3: Execute First Query
Make your first call to Claude using the query() function.
"""

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock, ToolUseBlock, ResultMessage
import asyncio
import os

# Configure options
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
    """Execute first query to Claude"""

    # TODO: Complete the prompt
    # Ask Claude to introduce itself
    prompt = ___  # TODO: Write "Hello Claude, please introduce yourself and explain what you can do with AWS"

    print("Executing first query to Claude...")
    print(f"Prompt: {prompt}\n")

    # TODO: Use async for loop to iterate over query() results
    # Pattern: async for message in query(prompt=prompt, options=options):
    async for message in ___:  # TODO: Complete this line
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
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
    with open("/root/markers/task3_first_query_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
