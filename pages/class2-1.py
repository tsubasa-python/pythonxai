print(len("apple"))  # lenは文字列の長さを返す関数
print(len(","))
# type
print(type(1))  # ｔypeはデータ型を返す関数
print(type(1.0))
print(type("apple"))
print(type(True))
print(type(False))


# boolとstrとintとfloatの変換
print(bool("apple"))
print(bool(1))
print(bool(1.0))
print(bool(True))
print(bool(False))
print(str(1))
print(str(1.0))
print(str("apple"))  # strは文字列型
print(str(True))  # boolはstrに変換できる
print(str(False))  # boolはstrに変換できない
print(int(1))  # intは整数型
print(int(1.0))  # floatからintに変換すると小数点以下が切り捨てられる

print(int(True))
print(int(False))
print(float(1))
print(float(1.0))
print(float(True))
print(float(False))

print("文字を入力してください")  # :=は代入演算子で、変数に値を代入する
a = input("パスワードを入力してください: ")  # inputはユーザーからの入力を受け取る関数
print(f"あなたが入力したパスワードは: {a}")  # f-stringを使って変数を文字列に埋め込む

b = input("数字を入力してください: ")
print(type(b))
print(int(b) + 10)

r = input("数字を入力してください: ")
print(3.14 * float(r) ** 2)  # 円の面積を計算する
