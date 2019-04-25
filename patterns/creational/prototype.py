"""
原型--对象创建型模式

1. 目标
根据原型实例指定创建对象的种类，并通过拷贝这些原型创建新的对象。

"""

import copy


class Prototype(object):
    """
    原型抽象类
    """
    def clone(self):
        raise NotImplementedError


class Cookbook(Prototype):
    def __init__(self, name):
        self.name = name
        self.menu = []

    def set_menu(self, dish_name):
        self.menu.append(dish_name)

    def clone(self, **attr):
        obj = copy.deepcopy(self)
        obj.__dict__.update(**attr)
        return obj

    def __repr__(self):
        return "Cookbook's name is %s, menu is %s" % (self.name, str(self.menu))


if __name__ == '__main__':
    cookbook1 = Cookbook('cookbook1')
    cookbook1.set_menu('menu1')
    print(cookbook1)

    cookbook2 = cookbook1.clone(name='cookbook2')
    cookbook2.set_menu('menu2')
    print(cookbook2)

