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

def get_groq_response(question):
    messages = [
        {
            "role": "system",
            "content":"You are 'BugSentinel', an expert chatbot specialized in Hacking and Bug Bounty. "
        "You provide precise, up-to-date, and ethical information on topics such as penetration testing, vulnerability assessment, exploit development, and web security. "
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

# Streamlit app title
st.title("BugSentinel - An expert chatbot specialized in Hacking and Bug Bounty")

# Display an image placeholder
st.image("Hacker.jpg", width=700, caption="Hacker")

# Adjust CSS for padding and text wrapping
st.markdown("""
<style>
.block-container {
    padding-top: 3rem;  /* Adjust this value as needed */
    padding-bottom: 1rem; /* Ensure bottom content is visible */
    padding-left: 1rem;
    padding-right: 1rem;
}
.css-1r6slb0 {
    white-space: normal !important;
}
.sidebar-text {
    white-space: normal !important;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)

# Input box for user query
query = st.text_input("Enter your query :")

# Button to get response
if st.button("Search"):
    if query:
        # Get the response from the Groq model
        response = get_groq_response(query)
        # Display the response
        st.write("Response:", response)
    else:
        st.write("Please enter a query.")

# Additional Streamlit widgets for beautification
st.sidebar.header("About This App")
st.sidebar.markdown('<div class="sidebar-text">This app allows you to ask questions about Hacking and Bug Bounty. Feel free to explore and learn more about Hacking and Bug Bounty!</div>', unsafe_allow_html=True)

# Add a footer
st.markdown("---")
st.markdown("Made with Streamlit")
