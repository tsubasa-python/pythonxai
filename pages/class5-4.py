import streamlit as st

st.chat_message("user").write("これは使用者からのメッセージです。")
st.chat_message("assistant").write("これはAIからのメッセージです。")

history = [
    {"role": "user", "content": "こんにちは。"},
    {"role": "assistant", "content": "こんにちは。何かお手伝いできますか？"},
    {"role": "user", "content": "これはどういうことですか？"},
    {"role": "assistant", "content": "st.chat_massage" "これは、チャットの例です。"},
]


for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
