#!/usr/bin/env python3
"""
Simple Agentic AI using local Model model via AI Navigator
Server: LOCAL:PORT
"""

import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from environment variables
# API_URL = os.getenv("API_URL")
MODEL = os.getenv("MODEL")
DEFAULT_TEMPERATURE = float(os.getenv("AGENT_TEMPERATURE"))
DEFAULT_MAX_TOKENS = int(os.getenv("AGENT_MAX_TOKENS"))
DEFAULT_TIMEOUT = int(os.getenv("AGENT_TIMEOUT"))
LOCAL = os.getenv("LOCAL")
PORT = os.getenv("PORT")
PATH = os.getenv("PATH")

API_URL = f"{LOCAL}:{PORT}{PATH}"


def call_model(messages, temperature=None, max_tokens=None):
    """Call the Model model via the local server."""
    # Use environment defaults if not provided
    if temperature is None:
        temperature = DEFAULT_TEMPERATURE
    if max_tokens is None:
        max_tokens = DEFAULT_MAX_TOKENS

    payload = {"model": MODEL, "messages": messages, "temperature": temperature, "max_tokens": max_tokens}
    try:
        response = requests.post(API_URL, json=payload, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error calling Model: {e}"


def read_file(path):
    """Read a file and return its contents."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f"✅ File content from {path}:\n{f.read()}"
    except Exception as e:
        return f"❌ Error reading file {path}: {e}"


def write_file(path, content):
    """Write content to a file."""
    try:
        # Create directory if path has one
        dir_path = os.path.dirname(path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ Successfully wrote content to {path}"
    except Exception as e:
        return f"❌ Error writing file {path}: {e}"


def calculate(expression):
    """Safely calculate mathematical expressions."""
    try:
        # Only allow safe mathematical operations
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            return "❌ Error: Invalid characters in expression"

        result = eval(expression, {"__builtins__": {}})
        return f"✅ Calculation result: {result}"
    except Exception as e:
        return f"❌ Error calculating '{expression}': {e}"


def get_time():
    """Get current date and time."""
    return f"✅ Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def list_files(directory="."):
    """List files in a directory."""
    try:
        files = os.listdir(directory)
        file_list = "\n".join(f"  - {f}" for f in files[:20])
        if len(files) > 20:
            file_list += f"\n  ... and {len(files) - 20} more files"
        return f"✅ Files in {directory}:\n{file_list}"
    except Exception as e:
        return f"❌ Error listing directory {directory}: {e}"


TOOLS = {
    "read_file": read_file,
    "write_file": write_file,
    "calculate": calculate,
    "get_time": get_time,
    "list_files": list_files,
}


def check_server():
    """Check if the Model server is running."""
    try:
        # Extract base URL from API_URL
        base_url = API_URL.replace("/v1/chat/completions", "")
        health_url = f"{base_url}/health"
        response = requests.get(health_url, timeout=5)
        return response.status_code == 200
    except Exception:
        return False


def run_agent():
    """Main agent loop for interactive chat."""
    print("🤖 Model Agent - Simple AI Assistant")
    print("=" * 40)
    print(f"Server: {API_URL}")
    print("Type 'exit', 'quit', or 'q' to stop")
    print("=" * 40)

    # Check server connection
    if not check_server():
        print("❌ Cannot connect to Model server!")
        print("Make sure your AI Navigator server is running on LOCAL:PORT")
        return

    print("✅ Connected to Model server")
    print()

    # Get system prompt from environment or use default
    system_prompt = os.getenv(
        "AGENT_SYSTEM_PROMPT",
        """You are a helpful AI assistant with access to tools. You can:
- Read files: read_file(path)
- Write files: write_file(path, content)
- Calculate math: calculate(expression)
- Get time: get_time()
- List files: list_files(directory)

When you need to use a tool, respond with JSON:
{"action": "tool_name", "parameters": {"param": "value"}}

For regular conversation, just respond naturally without JSON.""",
    )

    context = [{"role": "system", "content": system_prompt}]

    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            if user_input.lower() in ["exit", "quit", "q"]:
                print("👋 Goodbye!")
                break

            if not user_input:
                continue

            # Add user message to context
            context.append({"role": "user", "content": user_input})

            # Get response from Model
            reply = call_model(context)

            # Try to parse as JSON for tool use
            try:
                action_data = json.loads(reply)
                if "action" in action_data and action_data["action"] in TOOLS:
                    # Execute tool
                    tool_name = action_data["action"]
                    parameters = action_data.get("parameters", {})
                    tool_func = TOOLS[tool_name]

                    print(f"🛠️ Using {tool_name}...")
                    result = tool_func(**parameters)
                    print(f"📋 Result: {result}")

                    # Add tool result to context, split long line for lint
                    context.append({"role": "assistant", "content": f"Used {tool_name}: {result}"})
                else:
                    # Regular response
                    print(f"🤖 Model: {reply}")
                    context.append({"role": "assistant", "content": reply})
            except json.JSONDecodeError:
                # Regular conversation
                print(f"🤖 Model: {reply}")
                context.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_agent()
