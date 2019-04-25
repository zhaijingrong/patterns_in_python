"""
生成器--对象创建型模式

1. 目标
将一个复杂对象的构建与他的表示分离， 使得同样的构建过程可以创建不同的表示。

2. 与AbstractFactory的对比：
（1）Builder着重于构建， AbstractFactory着重于多个系列的产品对象。
（2）Builder可以认为是将Factory再封装，所以，Builder没有Factory灵活，而Builder对于固定类型的对象创建更方便。
    消费者如果想要组装不同类型的东西，比如奔驰的引擎和宝马的外壳，那只能使用Factory模式。

"""


class CarBuilder(object):
    def build_car(self):
        raise NotImplementedError

    def build_wheel(self):
        raise NotImplementedError

    def build_shell(self):
        raise NotImplementedError

    def build_engine(self):
        raise NotImplementedError

    def __repr__(self):
        return 'This is a car which has {0.wheel}, {0.shell} and {0.engine}'.format(self)


class BenzCarBuilder(CarBuilder):
    def build_car(self):
        self.build_wheel()
        self.build_shell()
        self.build_engine()

    def build_wheel(self):
        self.wheel = 'Benz wheel'

    def build_shell(self):
        self.shell = 'Benz shell'

    def build_engine(self):
        self.engine = 'Benz engine'


class BMWCarBuilder(CarBuilder):
    def build_car(self):
        self.build_wheel()
        self.build_shell()
        self.build_engine()

    def build_wheel(self):
        self.wheel = 'BMW wheel'

    def build_shell(self):
        self.shell = 'BMW shell'

    def build_engine(self):
        self.engine = 'BMW engine'


def construct_car(cls):
    car_builder = cls()
    car_builder.build_car()
    return car_builder


if __name__ == '__main__':
    print(construct_car(BMWCarBuilder))
    print(construct_car(BenzCarBuilder))