import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch the GROQ_API_KEY from the environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)
MODEL = 'llama3-70b-8192'

# Function to get response
def get_groq_response(question):
    messages = [
        {
            "role": "system",
            "content": "You are 'BugSentinel', an expert chatbot specialized in Hacking and Bug Bounty. "
                       "You provide precise, up-to-date, and ethical information on topics such as penetration testing, "
                       "vulnerability assessment, exploit development, and web security. "
                       "If someone asks a question outside the scope of ethical hacking and bug bounty, simply reply: "
                       "'I'm here to help with Hacking and Bug Bounty-related topics only. Let me know if you have any security-related queries!'"
        },
        {
            "role": "user",
            "content": question,
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=4096
    )

    return response.choices[0].message.content

# Initialize chat history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# App Title
st.title("🔍 BugSentinel - Hacking & Bug Bounty Assistant")

# Banner Image
st.image("image copy.png", width=700, caption="Hacking & Cybersecurity")

# CSS for Styling Chat
st.markdown("""
<style>
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 10px;
        background-color: #1E1E1E;
        color: white;
    }
    .message {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .user-message {
        background-color: #0078ff;
        color: white;
        padding: 8px 12px;
        border-radius: 15px;
        max-width: 75%;
        text-align: right;
    }
    .ai-message {
        background-color: #444;
        color: white;
        padding: 8px 12px;
        border-radius: 15px;
        max-width: 75%;
        text-align: left;
    }
    .user-container {
        justify-content: flex-end;
        text-align: right;
    }
    .ai-container {
        justify-content: flex-start;
    }
</style>
""", unsafe_allow_html=True)

# Chat History Section
st.markdown("## Chat History")
chat_placeholder = st.container()

with chat_placeholder:
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.markdown(f"""
            <div class='message user-container'>
                <div class='user-message'>{message['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='message ai-container'>
                <div class='ai-message'>{message['content']}</div>
            </div>
            """, unsafe_allow_html=True)

# User Input
st.markdown("## Ask BugSentinel")
query = st.text_input("Enter your query:")

if st.button("Search"):
    if query:
        response = get_groq_response(query)
        st.session_state.conversation.append({"role": "user", "content": query})
        st.session_state.conversation.append({"role": "assistant", "content": response})
        st.rerun()

# Sidebar Information
st.sidebar.header("📌 About This App")
st.sidebar.markdown("BugSentinel is an AI-powered chatbot that specializes in Hacking and Bug Bounty. "
                    "It provides guidance on ethical hacking, penetration testing, web security, and more.")

# Footer
st.markdown("---")
st.markdown("🚀 Developed by Sakshi Ambavade")
