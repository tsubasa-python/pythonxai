print(1 == 1)
print(1 != 1)  # false
print(1 > 1)  # false
print(1 < 1)  # false
print(1 >= 1)  # true
print(1 <= 1)  # true


print(True and True)  # true
print(True and False)  # false
print(False and True)  # false
print(False and False)  # false


print(not True)  # false
print(not False)  # true

# 優先する順番
# 1 ()
# 2 **
# 3 * / // %
# 4 + -
# 5 == != > < >= <=
# 6 not
# 7 and
# 8 or


password = input("パスワードを入力してください: ")
if password == "1234":
    print("パスワードが正しいです")
elif password == "abcd":
    print("こんにちは翼さん")
else:
    print("パスワードが間違っています")
