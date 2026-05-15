#!/usr/bin/env python3
"""
Lab 2 - Task 1: Terraform Discovery & Analysis
Combines Read, Glob, and Grep tools for comprehensive project analysis
"""
import os
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    """
    Perform comprehensive Terraform project analysis using discovery tools.

    This task demonstrates real-world workflow combining:
    - Glob: Find all Terraform files
    - Read: Inspect file contents
    - Grep: Search for patterns and issues
    """

    # TODO 1: Configure allowed tools
    # Hint: Set allowed_tools to ["Read", "Glob", "Grep"]
    # Expected: ["Read", "Glob", "Grep"]
    options = ClaudeAgentOptions(
        env={
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
            "ANTHROPIC_BASE_URL": os.getenv("ANTHROPIC_BASE_URL"),
        },
        model="claude-sonnet-4-6",
        allowed_tools=["Read", "Glob", "Grep"],
        permission_mode="acceptEdits",
        cwd="/root/code/terraform-project"
    )

    # TODO 2: Create comprehensive discovery prompt
    # Hint: Ask Claude to use all three tools to analyze the Terraform project
    # Expected: Multi-step prompt requesting Glob, Read, and Grep operations
    prompt = """
Perform comprehensive Terraform project analysis:

1. Use Glob to find all *.tf files in /root/code/terraform-project
2. Use Read to inspect each .tf file and identify:
   - Resource configurations
   - Syntax issues
   - Hardcoded values
3. Use Grep to search across all .tf files for:
   - "public-read" (security issue)
   - Hardcoded regions
   - Missing required configurations

Provide a detailed analysis report listing:
- All .tf files found
- Security issues discovered
- Syntax errors identified
- Recommendations for fixes
"""

    # TODO 3: Execute query and stream responses
    # Hint: Use async for loop to iterate over query() results
    # Expected: async for message in query(prompt=prompt, options=options)
    async for message in query(prompt=prompt, options=options):
        if hasattr(message, 'content'):
            for block in message.content:
                if hasattr(block, 'text'):
                    print(block.text)

    # TODO 4: Create completion marker
    # Hint: Create /root/markers/task1_discovery_complete.txt
    # Expected: Path should be /root/markers/task1_discovery_complete.txt
    os.makedirs('/root/markers', exist_ok=True)
    with open('/root/markers/task1_discovery_complete.txt', 'w') as f:
        f.write('Task 1: Terraform Discovery & Analysis completed successfully\n')
        f.write('Tools used: Read, Glob, Grep\n')

    print("\n" + "="*60)
    print("SUCCESS: Discovery analysis complete!")
    print("="*60)
    print("\nYou've learned to combine multiple discovery tools:")
    print("  - Glob: Finding files by pattern")
    print("  - Read: Inspecting file contents")
    print("  - Grep: Searching for specific patterns")
    print("\nThis is how real developers analyze codebases!")


if __name__ == '__main__':
    asyncio.run(main())
