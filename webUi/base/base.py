from selenium import webdriver


class PageBase(object):
    """
    对Selenium的第一层封装
    """
    def __init__(self, driver, base_url="https://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_test(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title


