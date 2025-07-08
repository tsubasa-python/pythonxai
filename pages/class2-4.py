import streamlit as st


number = st.number_input("数字を入力してください", step=1, min_value=0, max_value=100)
st.write(f"あなたが入力した数字は: {number}")  # f-stringを使って変数を文字列に埋め込む


st.write("練習")
points = st.number_input("点数を入力してください", step=1, min_value=0, max_value=100)
if points >= 90:
    st.write("s")
elif points >= 80:
    st.write("a")
elif points >= 70:
    st.write("b")
elif points >= 60:
    st.write("c")
else:
    st.write("f")
