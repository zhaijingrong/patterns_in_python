"""
单例--对象创建型模式

"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    pass


if __name__ == '__main__':
    logger1 = Logger()
    print(logger1)
    logger2 = Logger()
    print(logger2)