a = 1
a += 1
print(a)  # 2が表示される
a -= 1
print(a)  # 1が表示される
a *= 2
print(a)  # 2が表示される
a /= 2
print(a)  # 1が表示される
a //= 2
print(a)  # 0が表示される
a %= 2
print(a)  # 1が表示される
a **= 2
print(a)  # 1が表示される


# 1. ()
# 2 **
# 3. * / // %
# 4. + -
# 5 == != > < >= <=
# 6 not
# 7 and
# 8 or
# 9 = += -= *= /= //= %= **=


## 変数の初期化
# 変数の初期化は、最初に値を代入すること
i = 0
while i < 5:
    print(i)
    i += 1
    # 0 1 2 3 4 と表示される


while i < 5:
    print(i)
    for i in range(5):
        print(i)
        # 0 1 2 3 4 と表示される
    if i == 3:
        break
import random

print(random.randrange(7))  # 0から6までのランダムな整数を表示
print(random.randrange(1, 7))  #  # 1から6までのランダムな整数を表示
print(random.randrange(1, 7, 2))  # 1から6までの奇数を表示


print(random.randint(1, 6))  # 1から6までのランダムな整数を表示


ans = random.randint(1, 100)
while True:
    num = int(input("1から100の数字を入力してください: "))
    if num < ans:
        print("もっと大きい数字です")
    elif num > ans:
        print("もっと小さい数字です")
    else:
        print("正解です！")
        break  # 正解ならループを抜ける

d = {"リンゴ": 100, "バナナ": 200, "オレンジ": 150}
print(d)


d = {"リンゴ": 100, "バナナ": 200, "オレンジ": 150}
print(d["リンゴ"])  # 100が表示される


d = {"リンゴ": 100, "バナナ": 200, "オレンジ": 150}

for k in d:
    print(k)  # キーを表示
    print(d[k])  # 値を表示

for k in d.keys():
    print(k)  # キーを表示
    print(d[k])  # 値を表示

for v in d.values():
    print(v)  # 値を表示


for k, v in d.items():
    print(v)
for v in d.values():
    print(v)  # 値を表示

for k, v in d.items():
    print(f"{k}: {v}")  # キーと値を表示

d = {"リンゴ": 100, "バナナ": 200, "オレンジ": 150}
d["グレープ"] = 300  # 新しいキーと値を追加
print(d)
d["メロン"] = 400  # 新しいキーと値を追加
print(
    d
)  # {"リンゴ": 100, "バナナ": 200, "オレンジ": 150, "グレープ": 300, "メロン": 400} が表示される


d = {"リンゴ": 100, "バナナ": 200, "オレンジ": 150}
d["リンゴ"] = 120  # キー"リンゴ"の値を更新
print(d)  # {"リンゴ": 120, "バナナ": 200, "オレンジ": 150} が表示される


d = {"リンゴ": 100, "バナナ": 200, "オレンジ": 150}
d.pop("リンゴ")  # キー"リンゴ"を削除

popitem = d.pop(
    "メロン", "キーが存在しません"
)  # キー"メロン"が存在しない場合のデフォルト値を指定
print(d)
print(popitem)  # "キーが存在しません" が表示される
