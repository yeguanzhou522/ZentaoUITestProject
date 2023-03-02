from common.get_driver import GetDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.login import Login
import unittest
import time

class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        '''case03:使用 test01  12345aA 测试能否登录'''
        Login(self.driver, 'test01', '12345aA')
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()), '测试不通过')


if __name__ == '__main__':
    unittest.main(verbosity=2)
