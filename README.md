# Lab 1: Introduction to Claude Agent SDK - Code Files

This directory contains hands-on task files for learning Claude Agent SDK fundamentals.

## Task Files Overview

### Task 1: Import SDK Components (`task_1_imports.py`)
**Learning Objective**: Understand the core components of Claude Agent SDK
- Import `query` function for single-turn conversations
- Import `ClaudeAgentOptions` for configuration
- Import `asyncio` for async programming
- Import `os` for environment variables

**Key Concepts**:
- SDK uses async/await pattern
- Environment-based configuration (API keys, proxy URLs)

---

### Task 2: Configure ClaudeAgentOptions (`task_2_configure_options.py`)
**Learning Objective**: Learn how to configure the SDK for LiteLLM proxy

**Configuration Parameters**:
- `env`: Environment variables (ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL)
- `model`: Claude model name (claude-sonnet-4-6, claude-opus-4-6)
- `allowed_tools`: List of tools agent can use (Read, Write, Bash, etc.)
- `permission_mode`: How to handle tool execution (acceptEdits, plan, default)

**Key Concepts**:
- LiteLLM proxy routes claude-sonnet-4-6 to backend models
- Permission modes control automation vs manual approval
- Tool allowlists enhance security

---

### Task 3: First Query (`task_3_first_query.py`)
**Learning Objective**: Execute your first Claude Agent SDK query

**What You'll Do**:
- Create a simple prompt
- Call `query()` function with prompt and options
- Iterate through async response messages
- Print each message received

**Key Concepts**:
- `query()` is async and returns an async iterator
- Use `async for` to handle streaming responses
- Each iteration yields a message object

---

### Task 4: Extract Response Content (`task_4_extract_response.py`)
**Learning Objective**: Parse and extract text from SDK responses

**Message Types**:
- `AssistantMessage`: Contains Claude's text response
- `UserMessage`: Your original prompt
- `ResultMessage`: Tool execution results

**Key Concepts**:
- Check message type before accessing properties
- `AssistantMessage` has `.content` attribute
- `.content` is a list of content blocks

---

### Task 5: AWS Identity with Bash Tool (`task_5_aws_identity.py`)
**Learning Objective**: Use Bash tool for AWS CLI operations

**What You'll Do**:
- Configure SDK with Bash tool enabled
- Ask Claude to check AWS identity
- SDK executes `aws sts get-caller-identity` automatically

**Key Concepts**:
- Tools extend agent capabilities beyond conversation
- Bash tool enables command execution
- Agent decides when to use tools based on prompt

---

### Task 6: Message Flow (`task_6_message_flow.py`)
**Learning Objective**: Understand the complete message flow

**Message Flow**:
1. User sends prompt → UserMessage
2. Claude thinks → AssistantMessage (with reasoning)
3. Claude uses tool → ToolUse block
4. SDK executes tool → ResultMessage
5. Claude processes result → Final AssistantMessage

**Key Concepts**:
- Multiple messages in single query response
- Tools are transparent to user
- ResultMessage contains execution output and usage stats

---

## Environment Setup

### Pre-configured Variables
The lab environment has these variables configured:
- `ANTHROPIC_API_KEY`: LiteLLM proxy authentication
- `ANTHROPIC_BASE_URL`: http://localhost:4000 (LiteLLM proxy)
- `OPENAI_API_KEY`: Backend API authentication
- `OPENAI_API_BASE`: Backend API endpoint

### LiteLLM Proxy
- Running on port 4000
- Routes Claude model names to backend models
- Configured via `/root/config/config.yaml`

## Running Tasks

### Execution Order
Complete tasks in numerical order (1 → 6). Each task builds on previous concepts.

### Run a Task
```bash
cd /root/code
python3 task_1_imports.py
```

### Check Progress
```bash
ls /root/markers/
```

Each completed task creates a marker file in `/root/markers/`.

## Validation

Tasks are validated through:
1. **Marker Files**: Created on successful completion
2. **Test Commands**: SSH-based checks in questions.json
3. **Print Statements**: Visual confirmation of success

## Additional Files

### `verify_environment.py`
Checks that your lab environment is properly configured:
- Python virtual environment exists
- Claude Agent SDK installed
- LiteLLM proxy running
- Environment variables set

Run before starting tasks:
```bash
python3 /root/code/verify_environment.py
```

## Getting Help

### Common Issues

**Import Error**: SDK not installed
```bash
source /root/venv/bin/activate
python3 -c "import claude_agent_sdk; print('OK')"
```

**Connection Error**: Proxy not running
```bash
curl http://localhost:4000/health
cat /var/litellm.log
```

**Permission Error**: Marker directory doesn't exist
```bash
mkdir -p /root/markers
```

## Next Steps

After completing Lab 1:
- Lab 2: File Operations & Terraform
- Lab 3: Multi-turn Conversations & CloudFormation
- Lab 4: WebSearch & WebFetch Tools
- Lab 5: Skills System
- Lab 6: Subagents
- Lab 7: MCP Servers & Capstone

## Learning Resources

- [Claude Agent SDK Documentation](https://docs.anthropic.com/claude-agent-sdk)
- [LiteLLM Proxy Docs](https://docs.litellm.ai)
- [Claude API Reference](https://docs.anthropic.com/api)

---

**Note**: All task files contain TODOs with hints. Read comments carefully before completing each TODO.
