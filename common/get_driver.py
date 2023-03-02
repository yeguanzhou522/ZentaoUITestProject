from selenium import webdriver
from common.get_config import Config

def GetDriver():
    driver = webdriver.Chrome()
    driver.get(Config.read_ini('default', 'zentao_url'))
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    pass