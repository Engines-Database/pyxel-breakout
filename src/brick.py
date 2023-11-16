import pyxel
from entity import Entity


class Brick(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y, 16, 6, 0, 16, 16, 8)
