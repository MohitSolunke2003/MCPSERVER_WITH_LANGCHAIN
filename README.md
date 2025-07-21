# MCP Server with LangChain

This project implements an MCP-based server using LangChain and Groq's `qwen-qwq-32b` language model. It provides intelligent agent capabilities over the MCP protocol, with built-in endpoints for handling math and weather queries.

## 🔧 Features

- 🤖 Agent powered by Groq's `qwen-qwq-32b` model
- 🔗 LangChain integration for prompt management
- 🌐 MCP protocol-based communication
- 📐 Math API for solving expressions and equations
- ☀️ Weather API for retrieving current weather conditions

## 📁 Project Structure
root/
├── client.py # MCP client
├── main.py # Entry point for running the server
├── mathserver.py # Math-related MCP logic
├── weather.py # Weather-related MCP logic
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .env # Environment variables
├── LICENSE # License


## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MohitSolunke2003/MCPSERVER_WITH_LANGCHAIN.git
cd MCPSERVER_WITH_LANGCHAIN
```
# 2. Set up your environment
    Install dependencies:

    pip install -r requirements.txt

    Add your environment variables in a .env file (e.g., API keys, Groq credentials).

# 3. Run the server
    python main.py

    You can also run specific modules like:

    python mathserver.py
    python weather.py


# 🧠 Tech Stack

1. Python 3.x
2. LangChain
3. MCP Protocol
4. Groq (Qwen-QWQ-32B model)
5. Custom MCP Agents

✍️ Contributing
Feel free to fork and open PRs for improvements, bug fixes, or additional endpoints.



    


