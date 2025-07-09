import streamlit as st


st.write("### ボタン練習")
if st.button("これをおしてください", key="button1"):
    st.write("ボタン1が押されました！")
    st.balloons()
if st.button("これをおしてください", key="button2"):
    st.balloons()
if st.button("これをおしてください", key="button3"):
    st.snow()
st.write("---")


import streamlit as st

st.title("数字に応じたパターン表示")

# 数値入力
number = st.number_input(
    "数字を入力してください（1以上の整数）", min_value=1, step=1, max_value=9
)

# 結果表示
st.write("### 出力結果:")
for i in range(1, int(number) + 1):
    st.write(str(i) * i)
