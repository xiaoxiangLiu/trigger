
class EnvException(Exception):
    """
    测试环境异常
    """
    def __init__(self, ErrorMessage):
        super().__init__()
        self.ErrorMessage = ErrorMessage

    def __str__(self):
        return self.ErrorMessage


