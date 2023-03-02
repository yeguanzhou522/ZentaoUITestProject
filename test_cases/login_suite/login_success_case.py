from common.get_driver import GetDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.login import Login
import unittest
import time

class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver()

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    def test_login_1(self):
        '''case01:使用 test01  123456aA 测试能否登录'''
        Login(self.driver, 'test01', '123456aA')
        self.assertTrue(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h4.left-today'), '今天剩余工作总计'), '登录失败，测试不通过')

    def test_login_2(self):
        '''case02:使用 test02  123456aA 测试能否登录'''
        Login(self.driver, 'test02', '123456aA')
        self.assertTrue(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h4.left-today'), '今天剩余工作总计'), '登录失败，测试不通过')


if __name__ == '__main__':
    unittest.main(verbosity=2)
