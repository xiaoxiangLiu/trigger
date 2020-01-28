import requests
import pytest
from triger.common.base import login, logout


@pytest.fixture(scope="module")
def login_conftest(request):
    session = requests.session()
    print("this is request param username :{}".format(request.param['username']))
    print("this is request param password : {}".format(request.param['password']))
    login(session=session, username=request.param['username'], password=request.param['password'])
    print("this is requests login")
    yield session
    print("this is requests logout")
    logout(session=session)
    session.close()


@pytest.fixture(scope='session', autouse=True)
def fixture_session():
    print("fixture session")
    return "this is fixture session return"


# @pytest.fixture(scope='module', autouse=True)
# def fixture_module():
#     print("fixture module")
#     return "this is fixture module return"


@pytest.fixture(scope='class', autouse=True)
def fixture_class():
    print("fixture class")
    return "this is fixture class return"





