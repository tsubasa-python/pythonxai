# れんぞくで ifを使うと成功しないのでelifを使う
# elifは前の条件が満たされなかった場合に実行される
# このようにして、条件を満たすまでループさせる

for i in range(5):
    print(i)
    print("Hello World!")  # helloworld!を5回表示


for i in range(1, 5):
    print(i)
# 1 2 3 4 と表示される

for i in range(1, 10, 2):
    print(i)
