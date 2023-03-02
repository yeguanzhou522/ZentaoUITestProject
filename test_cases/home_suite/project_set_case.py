import unittest
import time
from common.get_driver import GetDriver
from common.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProjectSetCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver()

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()


    def test_projectset_link(self):
        '''case05:测试项目集按钮是否可跳转'''
        Login(self.driver, 'test01', '123456aA')
        self.driver.find_element(By.XPATH, '//*[@id="menuMainNav"]/li[2]/a/span').click()
        self.assertTrue((EC.text_to_be_present_in_element(By.LINK_TEXT, '项目集列表'), '项目集列表'), '测试不通过')


if __name__ == '__main__':
    unittest.main(verbosity=2)
