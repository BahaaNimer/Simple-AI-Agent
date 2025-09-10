# Simple Agent

A lightweight AI agent that connects to your local model server running via AI
Navigator. This agent can perform basic tasks like file operations,
calculations, and general conversation.

## 🚀 Features

- **Local Model Integration**: Connects to your existing model server
- **Simple Tools**: Basic file operations, calculations, and system utilities
- **Interactive Chat**: Clean command-line interface for conversation
- **No API Keys Required**: Uses your local model server

## 📁 Project Structure

```
agentic_ai_poc/
├── agent.py         # Main agent script
├── test_agent.py         # Test script to verify setup
├── requirements.txt      # Python dependencies
├── env.example           # Environment variables template
├── .gitignore           # Git ignore file
├── .flake8              # Flake8 configuration (120 char line limit)
├── pyproject.toml       # Modern Python project configuration
├── setup.cfg            # Legacy configuration for older tools
├── .vscode/             # VS Code settings
│   └── settings.json    # IDE configuration (120 char line limit)
└── README.md            # This file
```

## 🛠️ Setup

### Prerequisites

- Python 3.8+
- AI Navigator with your model running on `LOCAL:PORT`

### Installation

1. **Make sure your Qwen server is running:**

   ```bash
   # Your AI Navigator should show:
   # server is listening on LOCAL:PORT
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables (optional):**

   ```bash
   # Copy the example environment file
   cp env.example .env

   # Edit .env to customize settings (optional)
   # The agent will work with defaults if .env is not present
   ```

4. **Test the setup:**

   ```bash
   python test_agent.py
   ```

5. **Run the agent:**
   ```bash
   python agent.py
   ```

## 🎯 Usage

Simply run the agent and start chatting:

```bash
python agent.py
```

The agent will connect to your model server and provide an interactive chat
interface.

## 🔧 Available Tools

The agent has access to these simple tools:

- **File Operations**: Read, write, and list files
- **Calculator**: Perform mathematical calculations
- **Time**: Get current date and time
- **Directory Listing**: List files in directories

## 📝 Example Interactions

```
👤 You: Calculate 15 * 23 + 45
🤖 Model: I'll calculate that for you.
🛠️ Using calculate...
📋 Result: ✅ Calculation result: 390

👤 You: What files are in this directory?
🤖 Model: I'll list the files for you.
🛠️ Using list_files...
📋 Result: ✅ Files in .:
  - agent.py
  - requirements.txt
  - README.md
  - env_example.txt

👤 You: What time is it?
🤖 Model: I'll get the current time for you.
🛠️ Using get_time...
📋 Result: ✅ Current time: 2024-01-15 14:30:25
```

## ⚙️ Configuration

The agent can be configured using environment variables. Copy `env.example` to
`.env` and modify as needed:

### Environment Variables

- **`API_URL`**: Model server API endpoint
- **`MODEL`**: Model name
- **`AGENT_TEMPERATURE`**: Response creativity
- **`AGENT_MAX_TOKENS`**: Maximum response length
- **`AGENT_TIMEOUT`**: Request timeout in seconds
- **`AGENT_SYSTEM_PROMPT`**: Custom system prompt (optional)

### Example Configuration

```bash
# .env file
API_URL=
MODEL=
AGENT_TEMPERATURE=
AGENT_MAX_TOKENS=
AGENT_TIMEOUT=
```

## 🔧 Development

### Linting Configuration

The project is configured for 120-character line length across all tools:

- **Flake8**: `.flake8` and `pyproject.toml`
- **VS Code**: `.vscode/settings.json`
- **Legacy tools**: `setup.cfg`

To run linting:

```bash
flake8 .
```

## 🆘 Troubleshooting

### Common Issues

1. **Server Connection Error**

   - Make sure your AI Navigator server is running on `LOCAL:PORT`
   - Check that the server shows "server is listening on LOCAL:PORT"

2. **Import Errors**

   - Install dependencies: `pip install -r requirements.txt`

3. **Tool Execution Errors**

   - Check file permissions for file operations
   - Ensure file paths are correct

4. **Line Length Warnings**
   - The project uses 120-character line limit
   - If your IDE still shows 79-character warnings, restart it to pick up the
     new configuration

---

**Happy coding with your Model Agent! 🤖✨**
