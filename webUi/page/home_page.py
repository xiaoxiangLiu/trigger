from ..base.base import PageBase
from selenium.webdriver.common.by import By


class HomePage(PageBase):
    """
    第二层封装，页面元素分离，每个元素只定位一次
    """
    search_input = (By.ID, 'kw')  # 搜索输入框

    search_button = (By.ID, 'su')  # 搜索按钮

    def __init__(self, driver, base_url = 'https://www.baidu.com'):
        PageBase.__init__(self, driver, base_url)

    def openHomePage(self):
        print("打开首页：", self.base_url)
        self.driver.get(self.base_url)

    def input_search_test(self, text='selenium'):
        print("输入关键字：", text)
        self.input_test(self.search_input, text)

    def click_search_button(self):
        print("点击搜索按钮")
        self.click(self.search_button)



