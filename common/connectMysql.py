import pymysql
from .myExcetion import *
from .logger import logger


class ConnectMysql(object):

    """
    链接数据库
    """

    def __init__(self, env=1):
        """
        根据env类型来切换环境
        :param env: 测试环境代号
        """
        if env == 1:
            self.host = "localhost"
            self.user = "root"
            self.password = "root"
            self.db = "test"
            self.port = 3306

        else:
            raise EnvException

        try:
            self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                       port=self.port)
            self.cur = self.con.cursor()
        except Exception as e:
            print("测试环境：", self.host, "数据库链接错误：", e)

    def query_user_name(self, user_id):
        """
        根据用户id查询用户名称
        :param user_id: 用户id
        :return: 用户名
        """
        sql = "SELECT * FROMT USER_TABLE WHERE %s"
        try:
            self.cur.execute(sql, user_id)
            self.con.commit()
            user_id = self.cur.fetchall()
            return user_id
        except Exception as E:
            logger.error("查询用户ID错误：{}".format(E))
        self.cur.close()
