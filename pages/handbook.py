import streamlit as st
import os

folderPath = "markdown"
Files = os.listdir(folderPath)
print(Files)

Files.sort()

for f in Files:  # ファイル名がclass3で始まるものだけを表示
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        content = file.read()
    with st.expander(f[:-3]):
        st.write(content)
