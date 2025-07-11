import streamlit as st
import os

st.title("写真のアップロード")
st.image("image/1lnlydqh7at.jpeg", width=500)


image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

image_size = st.number_input(
    "写真の大きさ", min_value=1, max_value=500, value=100, step=10
)
for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
for image_file in image_files:

    st.image(f"{image_folder}/{image_file}", use_container_width=True)


selected_image = st.selectbox("写真の選択", image_files)
st.image(f"{image_folder}/{selected_image}", width=image_size)
