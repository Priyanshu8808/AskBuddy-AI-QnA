import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st


with st.sidebar:

    st.markdown( '<div class="sidebar-title">🤖 AskBuddy</div>', unsafe_allow_html=True )
    st.markdown("### 🤖 Model")
    st.info("GPT-OSS 20B\nPowered by Groq")
    st.markdown("### 💡 Try asking")
    examples = ["Explain machine learning simply","Write a Python program for Fibonacci","What is LangChain?","Explain SQL joins with examples"]
    for example in examples:
        st.markdown(f'<div class="example-box">💬 {example}</div>', unsafe_allow_html=True)
    st.markdown("---")

    if st.button( "🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")



llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.environ.get("GROQ_API_KEY")
)
st.title("AskBuddy - AI QnA Bot")
st.markdown("My QnA bot with LangChain and Groq")
# query = st.chat_input("Ask me anything!", key="unique_chat_input_key")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)  

query=st.chat_input("Ask me anything!")

if query:
      st.session_state.messages.append({"role": "user", "content": query})
      st.chat_message("user").markdown(query)
      res=llm.invoke(query)
      st.chat_message("AI").markdown(res.content)
      st.session_state.messages.append({"role": "assistant", "content": res.content})
      
      
      
##CSS Styling for the sidebar      


st.markdown("""
<style>


[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #0f172a 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
    padding-left: 1.2rem;
    padding-right: 1.2rem;
}



.sidebar-title {
    font-size: 1.65rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 1.5rem;
}


[data-testid="stSidebar"] h3 {
    color: #e5e7eb !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    margin-top: 1.2rem !important;
    margin-bottom: 0.7rem !important;
}


[data-testid="stSidebar"] .stAlert {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
    padding: 0.9rem !important;
}

[data-testid="stSidebar"] .stAlert p {
    color: #e5e7eb !important;
}




.example-box {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 10px 12px;
    margin: 8px 0;
    color: #d1d5db;
    font-size: 0.88rem;
    line-height: 1.35;
    transition: all 0.2s ease;
}

.example-box:hover {
    background: rgba(255,255,255,0.09);
    border-color: rgba(255,255,255,0.18);
    transform: translateX(3px);
}



[data-testid="stSidebar"] hr {
    border: none;
    height: 1px;
    background: rgba(255,255,255,0.10);
    margin: 1.3rem 0;
}


[data-testid="stSidebar"] button {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    background: rgba(255,255,255,0.05) !important;
    color: #e5e7eb !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

[data-testid="stSidebar"] button:hover {
    background: rgba(239,68,68,0.15) !important;
    border-color: rgba(239,68,68,0.4) !important;
    color: #fca5a5 !important;
}



[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: #d1d5db;
}



[data-testid="stSidebar"] ::-webkit-scrollbar {
    width: 5px;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-track {
    background: transparent;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.18);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)