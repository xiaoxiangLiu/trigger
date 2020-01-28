import requests
from .names import name
from .param import get_login_param
from ..common.tools import SwitchEnv


url, mysql_url, redis_url = SwitchEnv()


def login(session, username, password):
    """
    登陆接口
    :param session: session
    :param username: 用户名
    :param password: 用户密码
    :return:
    """
    session.get(url=url+name.login_url,
                data=get_login_param(username=username, password=password))
    return session


def logout(session):
    """
    退出登陆接口
    :param session:
    :return:
    """
    session.get(url=url+name.logout_url)

