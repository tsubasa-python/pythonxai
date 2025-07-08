import streamlit as st

with st.expander("class1 markdown"):
    st.write(
        '''# 🐍【Python 入門小筆記】

## ✏️ 註解是什麼？

-   註解的意思是「寫給人看的說明」，電腦不會執行這些文字。
-   有兩種方式可以寫註解：

```python
# 這是單行註解，只能寫一句話
"""
這是多行註解
可以寫很多行的說明
"""
```

👆 用來幫助自己或別人理解程式的用途。

---

## 👋 說哈囉！

```python
print("Hello World!")
```

-   `print()` 是顯示文字的指令，可以讓程式「說話」！

---

## 🔢 基本資料型態

電腦能認識不同種類的資料：

| 種類   | 範例            | 說明                       |
| ------ | --------------- | -------------------------- |
| 整數   | `1`, `-5`, `0`  | 沒有小數點的數字           |
| 小數   | `1.5`, `3.14`   | 有小數點的數字             |
| 文字   | `"apple"`       | 用引號包起來的字           |
| 布林值 | `True`, `False` | 只有「對」或「錯」兩種選擇 |

---

## 📦 變數：像小盒子一樣的東西

```python
a = 10
print(a)
a = "apple"
print(a)
```

-   把資料存在一個「名字」裡（像是 a），方便以後拿出來用。

---

## ➕ 運算子：讓電腦算數

| 運算 | 指令     | 結果 |
| ---- | -------- | ---- |
| 加法 | `1 + 1`  | 2    |
| 減法 | `5 - 3`  | 2    |
| 乘法 | `2 * 3`  | 6    |
| 除法 | `10 / 2` | 5.0  |
| 取商 | `9 // 2` | 4    |
| 餘數 | `9 % 2`  | 1    |
| 次方 | `2 ** 3` | 8    |

---

## 🔢 算式的優先順序

像數學一樣，電腦有算式的「先後順序」：

1. 括號 `()`
2. 次方 `**`
3. 乘、除、取商、餘數：`*`, `/`, `//`, `%`
4. 加減：`+`, `-`

---

## 🧵 字串（文字）的特別玩法

```python
print("apple" + " pen")  # 合併文字
print("apple " * 3)      # 重複文字
```

-   `+` 可以把兩段文字接在一起
-   `*` 可以重複文字很多次

---

## 🛠️ 小練習

```python   W
print("可以在終端機顯示文字")
a = "hello"
b = "world"
print(a + " " + b)
```

-   `print()` 可以讓電腦說出「你設定的內容」
-   把變數的內容組合起來也可以印出來！

---

## 🧩 f-string：讓文字可以自動帶入變數！

```python
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")
```

-   在字串前面加 `f`，裡面可以放變數，用 `{}` 包起來
-   這樣字串就可以「自動代入資料」啦！

---

## 📌 小提醒

-   如果要快速註解：按鍵盤上的 `Ctrl + ?`
-   寫程式時要多練習、多嘗試，錯誤是學習的一部分！
'''
    )
with st.expander("class2 markdown"):
    st.write(
        """


# 🐍 Python 初學者筆記：我今天學到的東西！

---

## 💡 基本知識

### ▶️ `print()`：把東西顯示出來

```python
print("Hello!")
```

### ▶️ `len()`：計算字的數量（字串長度）

```python
print(len("apple"))  # 5 個字母
print(len(","))      # 1 個符號
```

---

## 🔍 `type()`：看資料是什麼種類

```python
print(type(1))         # 是整數 int
print(type(1.0))       # 是小數 float
print(type("apple"))   # 是字串 str
print(type(True))      # 是布林值 bool（代表真或假）
print(type(False))     # 也是布林值
```

---

## 🔄 轉換資料的種類（型別）

### ✅ 轉成 `bool`（布林值：True 或 False）

```python
print(bool("apple"))   # 只要不是空的，就會是 True
print(bool(0))         # 0 是 False，其他數字是 True
print(bool(True))      # True
print(bool(False))     # False
```

### ✅ 轉成 `str`（字串）

```python
print(str(1))       # 變成 "1"
print(str(True))    # 變成 "True"
```

### ✅ 轉成 `int`（整數）

```python
print(int(1.0))     # 小數會去掉變整數
print(int(True))    # True 是 1，False 是 0
```

### ✅ 轉成 `float`（小數）

```python
print(float(1))     # 變成 1.0
print(float(True))  # 變成 1.0
```

---

## ⌨️ `input()`：讓使用者輸入東西

```python
a = input("請輸入密碼: ")
print(f"你輸入的密碼是: {a}")
```

### 加法練習（要轉成數字才能 +）

```python
b = input("請輸入數字: ")
print(int(b) + 10)
```

### 圓的面積（半徑 × 半徑 × 3.14）

```python
r = input("請輸入半徑: ")
print(3.14 * float(r) ** 2)
```

---

## ✅ 比大小和邏輯判斷

### 🧮 比大小符號

```python
print(1 == 1)   # 一樣嗎？是 True
print(1 != 1)   # 不一樣嗎？False
print(1 > 1)    # 比他大？False
print(1 >= 1)   # 大於或等於？True
```

### 🧠 邏輯運算

```python
print(True and True)   # 都要是 True 才是 True
print(True or False)   # 有一個 True 就是 True
print(not True)        # 相反，True 變 False
```

### 🎯 運算順序（誰先算？）

1. 括號 `()`
2. 次方 `**`
3. 乘除 `* /`
4. 加減 `+ -`
5. 比大小 `==, >, <`
6. `not`
7. `and`
8. `or`

---

## 🔐 判斷密碼的 if 條件

```python
password = input("請輸入密碼: ")
if password == "1234":
    print("密碼正確")
elif password == "abcd":
    print("你好，翼さん")
else:
    print("密碼錯誤")
```

---

## 🌐 Streamlit：做出網頁的小工具！

### 📘 顯示文字的方法

```python
import streamlit as st

st.title("這是標題")  # 大標題
st.write("這是普通文字")  # 顯示多種東西
st.text("這是純文字")  # 只能顯示文字
```

### ✨ Markdown 語法

````markdown
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼：
```python
print("Hello!")
````

````

### 📦 其他顯示方式
```python
st.info("這是資訊")
st.success("成功！")
st.warning("小心！")
st.error("錯誤！")
````

---

## 🧮 成績判斷小程式（Streamlit）

```python
points = st.number_input("請輸入分數", step=1, min_value=0, max_value=100)

if points >= 90:
    st.write("成績是 S")
elif points >= 80:
    st.write("成績是 A")
elif points >= 70:
    st.write("成績是 B")
elif points >= 60:
    st.write("成績是 C")
else:
    st.write("成績是 F")
```


"""
    )
