import streamlit as st  # Streamlitを使うための準備

st.title("買い物リスト")  # タイトルを表示

if "order" not in st.session_state:
    st.session_state.order = []  # セッション状態に注文リストを初期化

col1, col2 = st.columns(2)  # 2つのカラムを作成
with col1:
    itemInput = st.text_input("商品名を入力してください")  # 商品名の入力
with col2:
    if st.button("商品を追加", key="add_item"):
        st.session_state.order.append(itemInput)  # 商品を注文リストに追加

st.write("### 注文リスト")  # 注文リストのタイトル
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)  # 2つのカラムを作成
    with col1:
        st.write(st.session_state.order[i])  # 商品名を表示
    with col2:
        if st.button("戻す", key={i}):
            st.session_state.order.pop(i)
            st.rerun()  # 戻すボタンを押すと商品をリストから削除し、
