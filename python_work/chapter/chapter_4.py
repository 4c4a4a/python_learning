# 遍历打印整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # 单复数的命名利于理解阅读
    print(magician)
# for循环中更多操作
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
# 创建数值列表
for value in range(1, 5):  # 函数range()只会打印1,2,3,4,因为到5就停止，所以不会打印5
    print(value)

numbers = list(range(1, 6))  # 创建数值列表
print(numbers)

even_numbers = list(range(2, 11, 2))  # 可以指定步长，该例子创建了10以内的偶数
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)  # 创建前十个整数平方的列表
print(squares)
# 数值列表统计
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))
# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # 只访问列表中0~3索引，且到3停止，所以显示列表前三个元素
print(players[:2])  # 第一个索引未指定默认从头开始
print(players[3:])  # 终止索引未指定，默认到最后一个
print(players[-3:])  # 负数代表离列表末尾距离，-1代表最后一个，-2则是倒数第二
# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print((friend_foods))
# 元组，不可变的列表
dimensions = (200, 50)
# 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


