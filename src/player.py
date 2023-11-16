import pyxel
import constants
from entity import Entity

PLAYER_VELOCITY = 2
PLAYER_WIDTH = 24
PLAYER_HEIGHT = 4


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y, PLAYER_WIDTH, PLAYER_HEIGHT, 0, 8, 24, 8)
                               
    
    def _update(self):
        velx = 0

        if pyxel.btn(pyxel.KEY_LEFT):
            velx = -PLAYER_VELOCITY
        elif pyxel.btn(pyxel.KEY_RIGHT):
            velx = PLAYER_VELOCITY
            
        self.x += velx

        self.x = min(self.x, constants.SCREEN_WIDTH - PLAYER_WIDTH*0.5)
        self.x = max(self.x, PLAYER_WIDTH*0.5)
