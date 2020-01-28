import redis
from .logger import logger
from .myExcetion import *


class ConnectRedis(object):
    """
    链接redis
    """

    def __init__(self, env=1, host = "192.168.1.1", port=6379, db=6, password="123"):
        """
        初始化
        :param env: 测试环境参数
        """

        if env == 1:
            self.host = host
            self.port = port
            self.db = db
            self.password = password

        else:
            raise EnvException("redis测试环境异常！")

        try:
            self.pool = redis.ConnectionPool(host=self.host, port = self.port, db=self.db,password=self.password,
                                            decode_responses=True)
            self.conn = redis.Redis(connection_pool=self.pool)
        except Exception as E:
            logger.error("redis连接异常：{}".format(E))

    def clear_redis(self, name):
        """
        清除制定name或者是包含name的list的value
        :param name: redis的name，或者包含name的list
        :return:无
        """
        if isinstance(name, list):
            for i in name:
                index = self.conn.llen(i)
                for k in range(index):
                    self.conn.lpop(i)
        elif isinstance(name, str):
            if self.conn.llen(name) < 1:
                print("这个%s没有value", name)
            else:
                index = self.conn.llen(name=name)
                for i in range(index):
                    self.conn.lpop(name=name)
        else:
            logger.error("只接受str类型或者list类型")

