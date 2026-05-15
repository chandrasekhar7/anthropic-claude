#!/usr/bin/env python3
"""
Task 2: Configure ClaudeAgentOptions
Learn how to configure the agent for LiteLLM proxy connection.
"""

from claude_agent_sdk import ClaudeAgentOptions
import os

# Configure ClaudeAgentOptions for LiteLLM proxy
# This tells the SDK how to connect to Claude via LiteLLM

options = ClaudeAgentOptions(
    # Environment configuration for LiteLLM proxy
    env={
        # SOLUTION: Set ANTHROPIC_API_KEY from environment
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),

        # SOLUTION: Set ANTHROPIC_BASE_URL from environment
        "ANTHROPIC_BASE_URL": os.getenv("ANTHROPIC_BASE_URL"),
    },

    # SOLUTION: Set the model to "claude-sonnet-4-20250514"
    # This is a fast and cost-effective Claude model
    model="claude-sonnet-4-20250514",

    # SOLUTION: Set allowed_tools to ["Bash"]
    # This enables the Bash tool for AWS CLI commands
    allowed_tools=["Bash"],

    # SOLUTION: Set permission_mode to "acceptEdits"
    # This auto-approves tool execution
    permission_mode="acceptEdits",
)

print("SUCCESS: ClaudeAgentOptions configured")
print(f"Model: {options.model}")
print(f"Allowed tools: {options.allowed_tools}")
print(f"Permission mode: {options.permission_mode}")
print(f"LiteLLM proxy configured: {bool(options.env.get('ANTHROPIC_BASE_URL'))}")

# Create marker
os.makedirs("/root/markers", exist_ok=True)
with open("/root/markers/task2_options_complete.txt", "w") as f:
    f.write("SUCCESS")
