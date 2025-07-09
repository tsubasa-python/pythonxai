print([])
print([1, 2, 3])
print([1, 2, 3, "a", "b", "c"])
print([1, 2, 3, ["a", "b", "c"]])
print([1, True, "a", 1.23])


L = [1, 2, 3, "a", "b", "c"]
print(L[0])
print(L[1])
print(L[2])
print(L[3])

L = [1, 2, 3, "a", "b", "c"]
print(L[::2])  # このように、先頭から2つずつスライスする
print(L[1::4])  # このように、先頭から4つずつスライスする
print(L[1:4:2])

L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])

for i in L:
    print(i)

L = [1, 2, 3, "a", "b", "c"]
L[0] = 2
print(L)

a = 1
b = a
b = 2
print(a, b)  # aが１でbが２になる

a = [1, 2, 3]
b = a


L = [1, 2, 3]
L.append(4)
print(L)

L = ["a", "b", "c", "d", "e"]  # リストの末尾に4を追加
L.pop(4)
print(L)  # ["a", "b", "c", "d"] になる

for i in L:
    if i == "a":
        L.remove(i)
print(L)  # ["b", "c", "d"] になる
L = ["a", "b", "c", "d", "e"]
L.pop(0)
print(L)  # ["b", "c", "d", "e"] になる

L = [5, 2, 1, 3, 4]
L.sort()  # リストを昇順にソート
print(L)  # [1, 2, 3, 4, 5] になる

f = open("pages/class1-1.py", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()
# class 1-1.pyの内容を表示する
# ファイルを開く
# close()を忘れないようにする
with open("pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
# withを使うと自動的にclose()してくれる


filename = "class1.md"
print(filename.endswith(".md"))  # True
filename = "notes.txt"
print(filename.endswith(".md"))  # False
