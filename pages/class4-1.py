import streamlit as st


col1, col2 = st.columns(2)  # カラムの作成
col1.button("ボタン1", key="btn1")  # カラム1にボタンを配置
col2.button("ボタン2", key="btn2")  # カラム2にボタンを配置


col1, col2 = st.columns([1, 2])
col1.button("ボタン3", key="btn3")
col2.button("ボタン4", key="btn4")

col1, col2, col3 = st.columns([1, 2, 3])
col1.button("ボタン5", key="btn5")
col2.button("ボタン6", key="btn6")
col3.button("ボタン7", key="btn7")


col3.button("ボタン8", key="btn8")  # カラム3にボタンを配置
st.write("---")  # 区切り線を表示


col1, col2 = st.columns([1, 2])  # カラムの幅を指定
with col1:
    st.write("カラム1の内容")
    if st.button("ボタン9", key="btn9"):
        st.balloons()
with col2:
    st.write("カラム2の内容")
    st.button("ボタン10", key="btn10")
cols = st.columns(10)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"forのなかのボタン{i+1}", key=f"for_btn_{i+1}")


st.write("---")  # 区切り線を表示
st.write("columnsの練習")
col1, col2 = st.columns(2)  # 2つのカラムを作成
with col1:
    st.button("ボタン1", key="btn11")
    st.button("ボタン2", key="btn12")
    st.button("ボタン3", key="btn13")
with col2:
    st.write("カラム2の内容")
    st.write("これはカラム2の内容です。")
    st.write("これはカラム2の内容です。")
st.write("---")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"ボタン{i+1}", key=f"適当ボタン{i+4}")
    with col2:
        st.write(f"これは{i+1}回目のカラム2の内容です。")


st.write("---")  # 区切り線を表示
st.title("文字入力の練習")

text = st.text_input("文字を入力してください", value="初期値")
st.write("入力された文字:", text)

st.title("session_stateの練習")
ans = 1
if st.button("ansに1を代入", key="ans"):
    ans = ans + 1
st.write(f"ans={ans}")
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("ansボタン", key="ans2"):
    st.session_state.ans1 = st.session_state.ans1 + 1
st.write(f"ans={st.session_state.ans1}")

if st.button("ansをリセット", key="reset"):
    st.rerun()  # ページを再読み込みしてリセット
