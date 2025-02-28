import google.generativeai as genai
import streamlit as st

# 🔹 Set Google AI API Key
API_KEY = "AIzaSyCM8axF5gMnowgZp2nY_mWwo_ZvWq1lbhg"  # Apna Google API key yahan daalo
genai.configure(api_key=API_KEY)

# Function to get response from Gemini AI
def get_chat_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")  # Use Gemini AI model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit UI
st.title("💬 Google Gemini AI Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

chat_container = st.container()
with chat_container:
    for message in st.session_state["messages"]:
        role = "User" if message["role"] == "user" else "AI"
        st.markdown(f"**{role}:** {message['content']}")

user_input = st.text_input("Type your message...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    bot_reply = get_chat_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    st.rerun()
