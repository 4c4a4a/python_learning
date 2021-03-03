# 检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # and表示所有条件均满足才返回真
print(age_0 >= 21 or age_1 >= 21)  # or表示只要一个条件满足即返回真
# 判定特定值是否在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
# 判定特定值是否不在列表中
if 'banana' not in requested_toppings:
    print(f"Banana, you can post a response if you wish.")
# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
# if-elif-else结构
age = 12
if age < 4:
    print("You admission cost is $0.")
elif age < 18:# 中间可有多个elif代码块
    print("You admission cost is $25.")
else:
    print("You admission cost is $40.")
# 省略else代码块，else包罗万象，可能引入无效或恶意数据
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")



