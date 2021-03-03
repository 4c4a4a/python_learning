# 列表通常包含多个元素，用复数命名比较好
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
# 访问列表中最后一个元素
print(bicycles[-1])
# 修改列表元素
bicycles[0] = 'nike'
print(bicycles[0].title())
# 在列表中添加元素
bicycles.append('adidas')
print(bicycles[-1])
# 在列表中插入元素
bicycles.insert(0, 'lining')
print(bicycles[0].title())
# 删除元素del语句
del bicycles[0]
print(bicycles)
# 删除元素pop方法
popped_bicycles = bicycles.pop()
print(popped_bicycles)
print(bicycles)
# 根据值删除元素
bicycles.remove('nike')  # 只能删除第一个指定的值
print(bicycles)
# 方法sort()排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 永久排序
print(cars)
cars.sort(reverse=True)  # 反向永久排列
print(cars)
# 函数sorted()排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))  # 非永久排序
print(sorted(cars, reverse=True))  # 反向非永久排列
print("Here is the original list:")
print(cars)
# 倒着打印列表
cars.reverse()
print(cars)
# 确定列表长度
print(len(cars))

