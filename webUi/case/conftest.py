from selenium import webdriver
import pytest


@pytest.fixture(scope='function', autouse=True)
def fixture_function():
    driver = webdriver.Chrome()
    print("open driver")
    # driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.close()
