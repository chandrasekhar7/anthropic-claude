#!/usr/bin/env python3
"""
Task 5: Use MultiEdit Tool for Batch Changes
Learn how to use the MultiEdit tool to make multiple changes efficiently.
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
    # TODO: Add "Read" and "MultiEdit" to allowed_tools
    allowed_tools=["Read", "MultiEdit"],  # Line 18
    permission_mode="acceptEdits",
)

async def main():
    """Ask Claude to add missing security configurations using MultiEdit"""

    # TODO: Write prompt asking Claude to add encryption and versioning
    # Ask Claude to use MultiEdit to add both:
    # 1. S3 bucket encryption configuration
    # 2. S3 bucket versioning configuration
    # in a single operation
    prompt = "Use Read to examine /root/code/terraform-project/main.tf, then use MultiEdit to add BOTH S3 bucket encryption (AES256) and versioning configurations in a single operation"  # Line 30

    print("Asking Claude to add security configurations...\n")

    async for message in query(prompt=prompt, options=options):
        print(message)

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task3_multiedit_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
