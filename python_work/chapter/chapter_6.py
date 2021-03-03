# 简单示例
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# 修改字典中的值
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
# 删除键值对
del alien_0['speed']
print(alien_0)
# 存储不同对象的同一信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 使用方法get(),避免获取不存在的字典键值时出现错误,而是返回默认值
point_value = alien_0.get('points', 'No point value assigned.')  # 第二个参数没有设置时，默认显示为None
print(point_value)
# 遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():  # 方法items使字典返回一个键值对列表
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# 遍历字典中所有键，方法keys（），该方法会返回一个所有键值的列表
for name in favorite_languages.keys():  # 实际上，会默认遍历所有的键，因此将.keys()去掉结果仍然不变
    print(name.title())
# 按特定顺序遍历字典中的所有键
for name in sorted((favorite_languages.keys())):
    print(f"{name.title()}, thank you for taking the poll!")
# 遍历所有的值
for language in set(favorite_languages.values()):  # set()可以让列表中每个元素不重复而独一无二，并且这些元素创建集合
    print(language.title())
# 集合，可用一对花括号直接创建集合
languages = {'python', 'ruby', 'python', 'c'}
print(languages)  # 集合中的元素无重复





