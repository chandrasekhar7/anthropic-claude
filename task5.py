#!/usr/bin/env python3
"""
Task 5: AWS Identity Check with Bash Tool
Use the Bash tool to execute AWS CLI commands.
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
    # TODO: Add "Bash" to allowed_tools
    allowed_tools=___,  # TODO: ["Bash"]
    permission_mode="acceptEdits",
)

async def main():
    """Ask Claude to check AWS identity using Bash tool"""

    # TODO: Write prompt asking Claude to use Bash tool
    # Ask Claude to run: aws sts get-caller-identity
    prompt = ___  # TODO: "Use the Bash tool to run 'aws sts get-caller-identity' and show me the AWS account information"

    print("Asking Claude to check AWS identity...\n")

    async for message in query(prompt=prompt, options=options):
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
    with open("/root/markers/task5_aws_identity_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
