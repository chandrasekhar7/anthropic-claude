#!/usr/bin/env python3
"""
Task 1: Import Claude Agent SDK Components
Learn what components we need from the Claude Agent SDK.
"""

# Step 1: Import the query function
# This is the main function for single-turn conversations
from claude_agent_sdk import query  # SOLUTION: Import "query" from "claude_agent_sdk"

# Step 2: Import ClaudeAgentOptions
# This class configures the agent's behavior
from claude_agent_sdk import ClaudeAgentOptions  # SOLUTION: Import "ClaudeAgentOptions" from "claude_agent_sdk"

# Step 3: Import asyncio for async/await
# Claude Agent SDK uses async programming
import asyncio  # SOLUTION: Import "asyncio"

# Step 4: Import os for environment variables
# We'll need this for API keys and proxy configuration
import os  # SOLUTION: Import "os"

print("SUCCESS: Step 1 Complete - All components imported")
print("- query: Main function for single-turn conversations")
print("- ClaudeAgentOptions: Configuration for agent behavior")
print("- asyncio: For async/await programming")
print("- os: For environment variables")

# Create marker
import os as os_module
os_module.makedirs("/root/markers", exist_ok=True)
with open("/root/markers/task1_imports_complete.txt", "w") as f:
    f.write("SUCCESS")
