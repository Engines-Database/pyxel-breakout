import math_helper
import pyxel

class Entity():
    entities = []
    
    x = 0
    y = 0
    width = 0
    height = 0

    texture_x = 0
    texture_y = 0
    texture_width = 0
    texture_height = 0
    
    
    def __init__(
            self,
            x=0,
            y=0,
            width=0,
            height=0,
            texture_x=0,
            texture_y=0,
            texture_width=8,
            texture_height=8,
            *args,
            **kwargs):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture_x = texture_x
        self.texture_y = texture_y
        self.texture_width = texture_width
        self.texture_height = texture_height
        Entity.entities.append(self)


    def kill(self):
        Entity.entities.remove(self)
        

    def _update(self):
        pass

    
    def _draw(self):
        pass

    
    def update(self):
        self._update()

    
    def draw(self):
        self._draw()

        pyxel.blt(
            self.x - (self.texture_width * 0.5),
            self.y - (self.texture_height * 0.5),
            0,
            self.texture_x,
            self.texture_y,
            self.texture_width,
            self.texture_height,
            0)

        
    def get_intersection_rect(self, entity):
        return math_helper.get_intersection_rect(self, entity)
