#
message = "Hello python world!"
print(message)
# 字母开头大写
name1 = "liu gamma"
print(name1.title())
name2 = "LIU GAMMA"
print(name2.title())
# 全部大写或小写
name3 = "lIu GAmma"
print(name3.upper())
print(name3.lower())
# 拼接消息：
first_name = "ada"
last_name = "lovelace"
# 方法一
full_name1 = first_name + " " + last_name
print(full_name1)
# 方法二
full_name2 = f"{first_name} {last_name}"
print(full_name2)
print(f"Hello, {full_name2.title()}!")
# 制表符换行符添加空白
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# 删除空白
blank = " python  "
print(blank)
print(blank.rstrip())  # 字符末尾空白删除
print(blank.lstrip())  # 字符开头空白删除
print(blank.strip())  # 字符两端空白删除
# 表示为字符串
age = 23
print("Happy "+str(age)+"rd Birthday")
# 同时给多个变量赋值
x, y, z = 0, 0, 0
# 约定俗成，变量名字母全部大写视为常量
MAX_CONNECTIONS = 5000
# python之禅
# import this

