from .names import name
from .logger import logger


def SwitchEnv(env=127):
    """
    切换测试环境方法
    :param env:
    :return:
    """
    if env == 127:
        return name.env_url, name.env_251_mysql, name.env_251_redis
    else:
        pass


def assertResult(exResult,acResult,check):
    """
    结果校验
    :param exResult: 预期结果
    :param acResult: 实际结果
    :param check: 校验项目
    :return: flag
    """
    flag = None
    if exResult == acResult:
        flag = True
        logger.info("检验项目： {0}------预期结果：{1} ----  实际结果：{2} ----检验结果：{3}".format(check, exResult, acResult, flag))
    elif exResult != acResult:
        flag = False
        logger.error("检验项目： {0}------预期结果：{1} ----  实际结果：{2} ----检验结果：{3}".format(check, exResult, acResult, flag))
    return flag


def get_token(path, param={}):
    """
    接口的令牌加密方法
    :param path: url
    :param param: 接口参数
    :return:
    """
    if path:
        return param



