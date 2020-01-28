from triger.webUi.page.home_page import HomePage
import pytest


class TestSearch():

    def test_search(self, fixture_function):
        """
        搜索测试用例
        """
        baidu_driver = HomePage(driver=fixture_function, base_url='https://www.baidu.com')
        baidu_driver.openHomePage()
        baidu_driver.input_test(text="selenium")
        baidu_driver.click()

if __name__ == '__main__':
    pytest.main(['-s', 'test_search.py'])
