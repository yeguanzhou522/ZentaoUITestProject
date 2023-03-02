from common.get_driver import GetDriver
from selenium.webdriver.common.by import By


def Login(driver, username, password):
    driver.find_element(By.CSS_SELECTOR, 'input#account').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button#submit').click()


if __name__ == '__main__':
    Login('test01', '123456aA')