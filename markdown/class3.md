
---

## 🔁 **for文とif/elifの使い方**

```python
# れんぞくで ifを使うと成功しないのでelifを使う
# elifは前の条件が満たされなかった場合に実行される
# このようにして、条件を満たすまでループさせる

for i in range(5):
    print(i)
    print("Hello World!")  # Hello World! を5回表示
```

✅ `range(5)` で `0〜4` のループ。
✅ `print("Hello World!")` はその回数分、繰り返されます。

---

## 🖱️ **Streamlit のボタン練習**

```python
st.write("### ボタン練習")
if st.button("これをおしてください", key="button1"):
    st.write("ボタン1が押されました！")
    st.balloons()
if st.button("これをおしてください", key="button2"):
    st.balloons()
if st.button("これをおしてください", key="button3"):
    st.snow()
```

✅ `key` が重複しないように注意できていてOK！
✅ 各ボタンに別の反応をさせているのも良い練習です。

---

## 🔢 **数字入力 → 数字繰り返し出力（1〜9）**

```python
number = st.number_input(
    "数字を入力してください（1以上の整数）", min_value=1, step=1, max_value=9
)

for i in range(1, int(number) + 1):
    st.write(str(i) * i)
```

✅ 1〜9の数字に対応して正しく表示される。
✅ `str(i) * i` で `"333"` などの繰り返し表現も理解できていてバッチリです。

---

## 🧮 **リストの表示・スライス・forループ操作など**

```python
print([1, 2, 3, ["a", "b", "c"]])  # ネストされたリスト
print(L[::2])  # 0, 2, 4 番目の要素をスライス
print(L[1:4:2])  # インデックス1, 3 の要素
```

✅ スライスやループ処理を実際に試していて良いアプローチです。

---

## 🔄 **リストの変更・追加・削除**

```python
L = [1, 2, 3]
L.append(4)
L.pop(4)
L.remove("a")
```

✅ `.append()`、`.pop()`、`.remove()` を使ったリスト操作の理解ができています。

❗ 注意：`remove()` はループ中に使うと要素の削除によってインデックスがずれてバグが起きることも。例えば：

```python
# 推奨されない（要素を削除しながらループ）
for i in L:
    if i == "a":
        L.remove(i)
```

⚠️ このようなときは **コピーしてループする** のが安全：

```python
for i in L[:]:  # L[:] は L のコピー
    if i == "a":
        L.remove(i)
```

---

## 📂 **ファイルの読み込み**

```python
with open("pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

✅ `with open()` を使って、ファイルを自動的に閉じていて、とても良いです！

---

## ✅ **拡張子の判定**

```python
filename.endswith(".md")
```

✅ `.endswith()` を使って拡張子をチェックする方法も、実践的で良い学習です。

---

## ➕ おまけ：数字を1〜9までボタンで順に出力する Streamlit 例

Streamlitで、数字を1つずつ押すようなUIも作れます：

```python
import streamlit as st

st.title("数字をボタンで選ぶ")

for i in range(1, 10):
    if st.button(f"{i} を表示"):
        for j in range(1, i + 1):
            st.write(str(j) * j)
```

---
