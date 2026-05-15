#!/usr/bin/env python3
"""
Lab 2 - Task 4: Terraform Deployment (SOLUTION)
Combines file editing and Bash validation for safe infrastructure deployment
"""
import os
import asyncio
import time
from claude_agent_sdk import query, ClaudeAgentOptions
from utils import process_message, show_task_banner, show_completion


async def main():
    """
    Fix Terraform configuration, then validate and plan deployment.

    This task demonstrates real-world deployment workflow:
    - Step 1: Fix any syntax errors in main.tf
    - Step 2: Validate syntax (terraform validate)
    - Step 3: Create execution plan (terraform plan)
    - Step 4: Save deployment report
    """
    start_time = time.time()

    # Display task banner
    show_task_banner(4, "Terraform Deployment", ["Read", "Edit", "MultiEdit", "Bash", "Write"])

    # TODO 1: Configure allowed tools
    # Hint: Set allowed_tools including Write for deployment report
    # Expected: ["Read", "Edit", "MultiEdit", "Bash", "Write"]
    options = ClaudeAgentOptions(
        env={
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
            "ANTHROPIC_BASE_URL": os.getenv("ANTHROPIC_BASE_URL"),
        },
        model="claude-sonnet-4-6",
        allowed_tools=["Read", "Edit", "MultiEdit", "Bash", "Write"],
        permission_mode="acceptEdits",
        cwd="/root/code/terraform-project"
    )

    # TODO 2: Create comprehensive deployment prompt with error fixing
    # Hint: Ask Claude to first fix main.tf errors, then validate and plan
    # Expected: Multi-step prompt for fixing errors, validation, and planning
    prompt = """
Perform Terraform deployment with automatic error fixing:

STEP 1: Fix Configuration Errors
Use Read to examine /root/code/terraform-project/main.tf and identify syntax errors:
- Missing closing brace in terraform block (around line 8)
- Missing closing brace in aws_s3_bucket resource (around line 21)
- Incorrect syntax in versioning_configuration block (around line 26)

Use Edit or MultiEdit to fix all syntax errors:
1. Add missing closing brace for terraform block (after line 7)
2. Add missing closing brace for aws_s3_bucket resource (after line 20)
3. Fix versioning_configuration syntax (should be "versioning_configuration {" on line 26)

STEP 2: Validate Configuration
After fixing errors, run: terraform init (if not already initialized)
Then run: terraform validate
This checks for syntax errors and configuration issues.

STEP 3: Create Execution Plan
If validation passes, run: terraform plan -no-color
This shows what changes Terraform will make to infrastructure.

STEP 4: Generate and Save Deployment Report
Create a comprehensive deployment report including:
- Configuration fixes applied (what was fixed and where)
- Validation status (PASS/FAIL with details)
- Plan summary (S3 bucket and versioning resources to create)
- Recommendation (SAFE TO DEPLOY or NEEDS REVIEW)
- Timestamp and execution details

Use Write tool to save the report to /root/code/deployment_report.txt

If any step fails, diagnose the issue and provide detailed error information.
"""

    # TODO 3: Execute query and stream responses
    # Hint: Use async for loop with query()
    # Expected: async for message in query(prompt=prompt, options=options)
    async for message in query(prompt=prompt, options=options):
        await process_message(message)

    # Create completion marker (auto-created, not a learner task)
    os.makedirs('/root/markers', exist_ok=True)
    with open('/root/markers/task4_deployment_complete.txt', 'w') as f:
        f.write('Task 4: Terraform Deployment completed successfully\n')
        f.write('Configuration fixed, validation and planning workflow executed\n')

    elapsed = time.time() - start_time
    show_completion(4, elapsed)

    print("\n✨ What You've Learned:")
    print("  • Read & Edit Tools: Diagnose and fix configuration errors")
    print("  • Bash Tool: Execute system commands safely")
    print("  • Terraform Workflow: Fix → Validate → Plan → Apply")
    print("  • Error Handling: Always check and fix issues before deployment")
    print(f"\nDeployment report saved to: /root/code/deployment_report.txt")


if __name__ == '__main__':
    asyncio.run(main())
