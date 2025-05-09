﻿# Cognitive Layers

A sophisticated multi-layer cognitive system that processes user queries through various specialized layers, making intelligent decisions and taking appropriate actions.

## Project Structure

```
CognitiveLayers/
├── main.py              # Main entry point and orchestration
├── mcpserver.py         # MCP server implementation with tool definitions
├── layers/              # Core cognitive layers
│   ├── Decision.py     # Decision-making layer
│   ├── Memory.py       # Memory management layer
│   └── Perception.py   # Perception and fact extraction layer
├── pyproject.toml      # Project dependencies
└── .env                # Environment variables (not tracked in git)
```

## Architecture

The system is built with a layered architecture that processes information through multiple cognitive layers:

1. **Perception Layer**: Extracts facts and relevant information from user queries
2. **Memory Layer**: Manages context and maintains state across conversations
   - Stores passwords and credentials
   - Maintains conversation history
3. **Decision Layer**: Makes intelligent decisions based on:
   - Available tools
   - Current context
   - Previous conversations
   - User query

## Features

- **Iterative Processing**: Processes queries through multiple iterations for optimal results
- **Tool Integration**: Integrates with various tools through MCP (Mission Control Protocol)
- **Memory Management**: Maintains context and credentials across sessions
- **AI-Powered Decision Making**: Utilizes Google's Gemini AI for intelligent decision making

## Available Tools

- **AWS Console Login**: Secure access to AWS services
- **Deployment Tools**: Automated deployment capabilities
- **DSA Solver**: Problem-solving capabilities for Data Structures and Algorithms
- **Dynamic Greeting Resource**: Personalized greeting generation

## Setup

1. Clone the repository
2. Create a `.env` file with your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:
```bash
python main.py
```

The system will:
1. Initialize the MCP server
2. Establish connection
3. Process the user query through multiple iterations
4. Make decisions based on available tools and context
5. Execute appropriate actions

## Security

- Credentials are stored securely in the Memory layer
- AWS console access requires proper authentication
- Environment variables are used for sensitive API keys

## Dependencies

- Python 3.x
- MCP (Mondel Context Protocol)
- Google Gemini AI
- Additional dependencies listed in pyproject.toml

## Contributing

Feel free to submit issues and enhancement requests!
