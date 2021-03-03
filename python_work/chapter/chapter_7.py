# input(),此时的用户输入程序将理解为字符串
message = input("Tell me something, and I will repeat it back to you:")
print(message)
# int()获取数值输入
age = input("How old are you?")
age = int(age)
print(age)
# 求模运算符
print(4 % 3)  # 取余数
# while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n(Enter 'quit' to end the program.)"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# 使用标志
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# continue 返回循环的开头重新执行
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:  # 打印所有奇数
        continue
    print(current_number)
# break 退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")




