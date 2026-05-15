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
        # TODO: Set ANTHROPIC_API_KEY from environment
        # Hint: Use os.getenv("ANTHROPIC_API_KEY")
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),

        # TODO: Set ANTHROPIC_BASE_URL from environment
        # Hint: Use os.getenv("ANTHROPIC_BASE_URL")
        "ANTHROPIC_BASE_URL": ___,
    },

    # TODO: Set the model to "claude-sonnet-4-6"
    # This is a fast and cost-effective Claude model
    model=___,

    # TODO: Set allowed_tools to ["Bash"]
    # This enables the Bash tool for AWS CLI commands
    allowed_tools=___,

    # TODO: Set permission_mode to "acceptEdits"
    # This auto-approves tool execution
    permission_mode=___,
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
