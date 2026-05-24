# LangGraph AI Agent Chatbot

A production-style AI chatbot built using **LangGraph**, **LangChain**, **OpenAI**, and **Streamlit**.

This application demonstrates how to build an AI agent capable of:

* Tool Calling
* Streaming Responses
* Persistent Memory
* Multi-Thread Conversations
* Web Search
* Stock Price Retrieval
* Calculator Operations

The chatbot uses LangGraph state-based workflows with memory checkpointing and intelligent tool routing.

---

# ✨ Features

* 🤖 AI Agent with LangGraph
* 💬 Real-time streaming responses
* 🧠 Persistent chat memory
* 🔀 Multi-conversation support
* 🔧 Intelligent tool calling
* 🌐 Web search integration
* 📈 Stock price lookup
* ➗ Calculator tool
* ⚡ Clean Streamlit UI
* 🗂️ Conversation thread management

---

# 🛠️ Tech Stack

* Python
* Streamlit
* LangGraph
* LangChain
* OpenAI API
* SQLite
* DuckDuckGo Search
* AlphaVantage API

---

# 📂 Project Structure

```bash
.
├── langgraph_tool_backend.py
├── langgraph_tool_frontend.py
├── chatbot.db
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git

cd your-repo-name
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
ALPHAVANTAGE_API_KEY=your_alpha_vantage_api_key
```

---

# ▶️ Run the App

```bash
streamlit run langgraph_tool_frontend.py
```

---

# 🧠 Tools Included

## 🌐 Web Search Tool

Uses DuckDuckGo Search for retrieving real-time web information.

Example:

```text
Search latest AI news
```

---

## ➗ Calculator Tool

Supports:

* Addition
* Subtraction
* Multiplication
* Division

Example:

```text
Calculate 245 * 89
```

---

## 📈 Stock Price Tool

Fetches live stock prices using AlphaVantage API.

Example:

```text
What is the stock price of Tesla?
```

---

# 🧠 How It Works

1. User sends a message
2. LangGraph processes conversation state
3. LLM decides whether a tool is required
4. Tool executes if needed
5. Response streams back to UI
6. Conversation state saved in SQLite

---

# 📄 Core Components

## LangGraph Workflow

Handles:

* State management
* Tool routing
* Memory persistence
* Conversation flow

---

## Streamlit Frontend

Handles:

* Chat UI
* Streaming responses
* Conversation switching
* Session management

---

## SQLite Checkpointing

Stores conversation history using:

```python
SqliteSaver
```

---

# 🔥 Example Questions

```text
Search latest AI developments

What is the stock price of NVIDIA?

Calculate 756 / 12

Who won the Cricket World Cup?

Explain quantum computing simply
```

---

# 🚧 Future Improvements

* PostgreSQL persistence
* User authentication
* RAG integration
* File upload support
* Browser automation agents
* Multi-agent systems
* Voice assistant
* Internet browsing agents
* Long-term memory

---

# 📌 Requirements

* Python 3.10+
* OpenAI API Key

---

# ⚠️ Important Notes

## SQLite Persistence

This project currently uses SQLite for memory persistence.

On local machines:

* conversations persist normally

On Streamlit Cloud:

* persistence may reset after redeployment/restart

For production deployments:

* PostgreSQL
* Supabase
* NeonDB

are recommended.

---

# 🔒 Privacy Update

Conversation threads are isolated per browser session to prevent users from accessing each other's chats.

---

# 🌐 Deployment

Recommended platforms:

* [Streamlit Community Cloud](https://streamlit.io/cloud?utm_source=chatgpt.com)
* [GitHub](https://github.com?utm_source=chatgpt.com)

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Ayush Kumar
