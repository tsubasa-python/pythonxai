import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []
for message in st.session_state.history:
    st.chat_message("user", avatar="👤").write(message["content"])

prompt = st.chat_input("プロンプトを入力してください")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
