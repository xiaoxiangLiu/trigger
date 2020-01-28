import pytest


login_test_data = [{'username':"admin1", 'password':"123456"},
                   {"username":"admin2", "password":"456789"}]
@pytest.mark.parametrize(("login_conftest"), login_test_data, indirect=True)
def test_login(login_conftest):
    print(login_conftest)


if __name__ == '__main__':
    pytest.main(['test_example.py', '-s'])




