# 打开pi_digits文件
with open('pi_digits.txt') as file_object:  # 关键字with让文件在使用完后自动关闭
    contents = file_object.read()
print(contents)

# 逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建包含各行内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 写入文件
filename = 'programming.txt'

with open(filename, 'w') as file_object:  # 'w'指以写入模式打开这个文件，其他详情看《python从入门到实践》P172
    file_object.write("I love programming.")

# 处理ZeroDivisionError异常
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 存储数据
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
with open(filename) as f:
    numbers = json.load(f)

print(numbers)




