import streamlit as st
from langgraph_tool_backend import chatbot
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import uuid

# ========================= UTILITIES =========================

def generate_thread_id():
    return str(uuid.uuid4())


def reset_chat():
    thread_id = generate_thread_id()

    st.session_state["thread_id"] = thread_id
    st.session_state["message_history"] = []
    st.session_state["chat_threads"].append(thread_id)


def clear_current_chat():
    st.session_state["message_history"] = []


# ========================= SESSION STATE =========================

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = []

if st.session_state["thread_id"] not in st.session_state["chat_threads"]:
    st.session_state["chat_threads"].append(
        st.session_state["thread_id"]
    )

# ========================= SIDEBAR =========================

st.sidebar.title("LangGraph AI Agent")

if st.sidebar.button("➕ New Chat"):
    reset_chat()

if st.sidebar.button("🗑️ Clear Current Chat"):
    clear_current_chat()

st.sidebar.markdown("---")

st.sidebar.subheader("Conversations")

for idx, thread_id in enumerate(
    reversed(st.session_state["chat_threads"])
):

    button_name = f"Chat {len(st.session_state['chat_threads']) - idx}"

    if st.sidebar.button(button_name, key=thread_id):

        st.session_state["thread_id"] = thread_id
        st.session_state["message_history"] = []

# ========================= MAIN CHAT =========================

st.title("🤖 LangGraph AI Agent")

# Render previous messages
for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Store user message
    st.session_state["message_history"].append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Render user message
    with st.chat_message("user"):
        st.markdown(user_input)

    CONFIG = {
        "configurable": {
            "thread_id": st.session_state["thread_id"]
        }
    }

    # Assistant response
    with st.chat_message("assistant"):

        status_holder = {"box": None}

        def ai_only_stream():

            for message_chunk, metadata in chatbot.stream(
                {
                    "messages": [
                        HumanMessage(content=user_input)
                    ]
                },
                config=CONFIG,
                stream_mode="messages",
            ):

                # Tool status
                if isinstance(message_chunk, ToolMessage):

                    tool_name = getattr(
                        message_chunk,
                        "name",
                        "tool"
                    )

                    if status_holder["box"] is None:

                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` ...",
                            expanded=True
                        )

                    else:

                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` ...",
                            state="running",
                            expanded=True,
                        )

                    continue

                # Stream only AI text
                if isinstance(message_chunk, AIMessage):

                    content = message_chunk.content

                    if isinstance(content, str):

                        cleaned = content.strip()

                        if cleaned:
                            yield cleaned

        ai_response = st.write_stream(ai_only_stream())

        # Tool completion UI
        if status_holder["box"] is not None:

            status_holder["box"].update(
                label="✅ Tool finished",
                state="complete",
                expanded=False,
            )

    # Save assistant response
    st.session_state["message_history"].append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )