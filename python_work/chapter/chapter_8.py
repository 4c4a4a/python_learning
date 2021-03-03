# 定义函数
def greet_user(username):
    """显示简单的问候语"""  # 文档字符串，生成有关程序中函数的文档
    print(f"Hello, {username.title()}!")


greet_user('Jack')


# 位置实参，要求实参与形参顺序相同
def describe_pet(animal_type, pet_name='jack'):  # 在定义时对形参赋值即设定默认值，必须先列没默认值的形参，再列有默认值的
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('burger', 'harry')
# 关键字实参，传递给函数的名称值对，不用考虑顺序
describe_pet(animal_type='hamster', pet_name='handsome')


# 返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变为可选的
def get_formatted_name(first_name, last_name, middle_name=''):  # 这个例子中，实参middle_name是可以不填的
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# 传递任意数量的实参
def make_pizza(size, *toppings):  # 若有多个形参，容纳任意数量的形参必须放在最后，先匹配之前的位置实参和关键字实参，余下的收集到最后一个形参(列表)
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):  # 两个星号创建一个字典
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
# 模块，存储函数代码的独立文件，将模块导入到主程序中，使主程序简洁易懂
'''模块是扩展名为.py的文件'''
from practice import practice_8, practice_8 as p8

practice_8.make_pizza(16, 'pepperoni')
practice_8.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''如果要导入特定的函数而不是整个文件，
   可用 "from module_name import function_1, function_2"这个语法，
   这种情况下，调用函数无需用句点,直接指定即可'''

# 使用as给函数或模块指定别名
from practice.practice_8 import make_pizza as mp

mp(16, 'pepperoni')

p8.make_pizza(16, 'pepperoni')

# 导入模块中的所有函数



