"""
抽象工厂--对象创建型模式。

1. 目标
提供一个创建一系列相关或相互依赖对象的接口， 而无需指定他们具体的类。

"""


class MazeFactory(object):
    """
    A maze factory
    """

    def __init__(self):
        print('Initial a maze!')

    def make_maze(self):
        print('make a maze')

    def make_wall(self):
        print('make a wall')

    def make_room(self, n):
        print('make a room %s' % n)
        return 'room %s' % n

    def make_door(self, r1, r2):
        print('make a door between %s and %s' % (r1, r2))


class EnchantedMazeFactory(MazeFactory):
    """
    A enchanted maze factory
    """

    def __init__(self):
        print('Initial a enchanted maze!')

    def make_room(self, n):
        print('make enchanted room %s' % n)
        return 'room %s' % n

    def make_door(self, r1, r2):
        print('make a door needing spell between %s and %s' % (r1, r2))


class BombedMazeFactory(MazeFactory):
    """
    A boomed maze factory
    """

    def __init__(self):
        print('Initial a bombed maze')

    def make_wall(self):
        print('make a bombed wall')

    def make_room(self, n):
        print('make a room %s with a bomb' % n)
        return 'room %s' % n


def create_maze(factory):
    a_maze = factory.make_maze()
    r1 = factory.make_room(1)
    r2 = factory.make_room(2)
    a_door = factory.make_door(r1, r2)


if __name__ == '__main__':
    enchanted_maze_factory = EnchantedMazeFactory()
    create_maze(enchanted_maze_factory)

    bombed_maze_factory = BombedMazeFactory()
    create_maze(bombed_maze_factory)