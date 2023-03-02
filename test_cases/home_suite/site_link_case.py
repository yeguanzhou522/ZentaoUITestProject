from common.get_driver import GetDriver
from common.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class SiteLinkCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_sit_link(self):
        '''case04:测试地盘按钮是否可跳转'''
        Login(self.driver, 'test01', '123456aA')
        self.driver.find_element(By.XPATH, '//*[@id="menuMainNav"]/li[1]/a/span').click()
        self.assertTrue(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h4.left-today'), '今天剩余工作总计'), '登录失败，测试不通过')


if __name__ == '__main__':
    unittest.main(verbosity=2)