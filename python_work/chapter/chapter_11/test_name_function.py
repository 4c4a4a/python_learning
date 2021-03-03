# 可通过的测试
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):  # 用于包含一系列对目标函数的单元测试，必须继承unittest.TestCase类
    """测试name_function.py"""
    def test_first_last_name(self):  # test_打头的方法将自动执行
        """能够正确处理Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # 断言方法，判断结果与期望是否一致
        
    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':  # __name__这个变量是在程序执行时设置，这个文件作为主程序执行时，__name__将被设为__main__
    unittest.main()  # 调用unittest.main()来运行测试用例,文件被测试框架导入，__name__不再是__main__，不会调用unittest.main()




