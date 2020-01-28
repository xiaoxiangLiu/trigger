from .tools import get_token
from .names import name


def example(path, param={}, **kwargs):
    """
    举例说明参数封装函数
    :param kwargs:
    :return:
    """
    if param:
        token_param = get_token(path=path,param=param)
        return token_param
    else:
        token_param = get_token(path=path, param=kwargs)
        return token_param


def get_login_param(path='gin', param={}, **kwargs):
    """
    登陆接口参数加密组装
    :param kwargs:
    :return:
    """
    if param:
        token_param = get_token(path=path,param=param)
        return token_param
    else:
        token_param = get_token(path=path, param=kwargs)
        return token_param


