import configparser
import os

current = os.path.dirname(__file__)
conf_filepath = os.path.join(current, '../conf/config.ini')

class GetConfig:
    def __init__(self, conf_path=conf_filepath):
        self.__conf_path = conf_path
        self.__conf = configparser.ConfigParser()
        self.__conf.read(self.__conf_path, encoding='utf-8')

    def read_ini(self, section, option):
        return self.__conf.get(section, option)

Config = GetConfig()
if __name__ == '__main__':
    pass