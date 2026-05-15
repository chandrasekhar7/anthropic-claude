#!/usr/bin/env python3
"""
Task 4: Use Edit Tool to Fix Syntax Errors
Learn how to use the Edit tool to make targeted changes to files.
"""

from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio
import os

options = ClaudeAgentOptions(
    env={
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        "ANTHROPIC_BASE_URL": os.getenv("ANTHROPIC_BASE_URL"),
    },
    model="claude-sonnet-4-6",
    # TODO: Add "Read" and "Edit" to allowed_tools
    allowed_tools=["Read", "Edit"],
    permission_mode="acceptEdits",
)

async def main():
    """Ask Claude to fix missing closing braces in main.tf"""

    # TODO: Write prompt asking Claude to fix syntax errors
    # Ask Claude to use Read to examine /root/code/terraform-project/main.tf
    # and then use Edit to fix ALL missing closing braces
    prompt = "Use Read to examine /root/code/terraform-project/main.tf and then use Edit to fix all missing closing braces in the Terraform blocks"

    print("Asking Claude to fix syntax errors...\n")

    async for message in query(prompt=prompt, options=options):
        print(message)

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task2_edit_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
