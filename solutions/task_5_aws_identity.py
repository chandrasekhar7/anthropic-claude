#!/usr/bin/env python3
"""
Task 5: AWS Identity Check with Bash Tool
Use the Bash tool to execute AWS CLI commands.
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
    # SOLUTION: Add "Bash" to allowed_tools
    allowed_tools=["Bash"],
    permission_mode="acceptEdits",
)

async def main():
    """Ask Claude to check AWS identity using Bash tool"""

    # SOLUTION: Write prompt asking Claude to use Bash tool
    prompt = "Use the Bash tool to run 'aws sts get-caller-identity' and show me the AWS account information"

    print("Asking Claude to check AWS identity...\n")

    async for message in query(prompt=prompt, options=options):
        print(message)

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task5_aws_identity_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
