#!/usr/bin/env python3
"""
Task 6: Use Write Tool to Create Missing Files
Learn how to use the Write tool to create new files from scratch.
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
    # TODO: Add "Read" and "Write" to allowed_tools
    allowed_tools=["Read", "Write"],  # Line 18
    permission_mode="acceptEdits",
)

async def main():
    """Ask Claude to complete outputs.tf using Write tool"""

    # TODO: Write prompt asking Claude to create complete outputs.tf
    # Ask Claude to use Read to see the current /root/code/terraform-project/outputs.tf
    # and then use Write to create a complete outputs.tf with all needed outputs:
    # - bucket_name, bucket_arn, website_endpoint, cloudfront_distribution_id, cloudfront_domain_name
    prompt = "Use Read to examine /root/code/terraform-project/outputs.tf and main.tf, then use Write to create a complete outputs.tf file with outputs for: bucket_name, bucket_arn, website_endpoint, cloudfront_distribution_id, and cloudfront_domain_name"  # Line 29

    print("Asking Claude to create complete outputs file...\n")

    async for message in query(prompt=prompt, options=options):
        print(message)

    # Create marker
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task4_write_complete.txt", "w") as f:
        f.write("SUCCESS")

if __name__ == "__main__":
    asyncio.run(main())
