# 创建dog类
class Dog:  # 根据约定，首字母大写的名称指的是类
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):  # 类中的函数叫做方法
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗受到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗受到命令时打滚"""
        print(f"{self.name} rolled over!")


# 创建实例
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()


#
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        设置里程表
        并禁止往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """增加指定里程"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值
my_new_car.odometer_reading = 23  # 直接访问修改
my_new_car.read_odometer()

my_new_car.update_odometer(25)  # 通过方法修改
my_new_car.increment_odometer(4)  # 通过方法递增
my_new_car.read_odometer()


# 将实例用作属性
class Battery:
    def __init__(self):
        self.battery_size =75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


# 继承
class ElectricCar(Car):  # 创建子类时，父类必须在文件中，且在子类前面
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # super让我们可以调用父类的方法
        self.battery = Battery()  # 后面还可以定义一些特有的函数


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# 如果想要重写父类方法，只要在子类定义一个同名方法即可

# 将实例用作属性
my_tesla.battery.describe_battery()












