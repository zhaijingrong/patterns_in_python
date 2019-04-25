"""
抽象工厂方法--对象创建型模式

1. 目标
定义一个用于创建对象的接口， 让子类决定实例化哪一个类， 使一个类的实例化延迟到子类。

"""

class CakeFactory(object):
    def make_cake(self):
        print('make a cake')


class CreamCakeFactory(CakeFactory):
    def make_cake(self):
        print('make a cream cake')
        return CreamCake()


class FruitCakeFactory(CakeFactory):
    def make_cake(self):
        print('make a fruit cake')
        return FruitCake()


class Cake(object):
    def __repr__(self):
        return 'This is a cake'


class CreamCake(Cake):
    def __repr__(self):
        return 'This is a cream cake'


class FruitCake(Cake):
    def __repr__(self):
        return 'This is a fruit cake'


if __name__ == '__main__':
    cream_cake_factory = CreamCakeFactory()
    cream_cake = cream_cake_factory.make_cake()
    print(cream_cake)

    fruit_cake_factory = FruitCakeFactory()
    fruit_cake = fruit_cake_factory.make_cake()
    print(fruit_cake)