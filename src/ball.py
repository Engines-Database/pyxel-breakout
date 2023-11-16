import math
import math_helper
import pyxel
import constants
import player
from entity import Entity

MIN_ANGLE = math.pi / 6.0
BALL_VELOCITY = 3

class Ball(Entity):
    vel = math_helper.rotate_vector([-BALL_VELOCITY, 0],math.pi + math.pi*0.25)
    player = None
    score_manager = None
    
    
    def __init__(self, x, y, player, score_manager, *args, **kwargs):
        self.player = player
        self.score_manager = score_manager
        Entity.__init__(self, x, y, 4, 4, 0, 0, 8, 8)
        
    
    def _update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]

        if self.x < 0 or self.x > constants.SCREEN_WIDTH:
            self.vel[0] *= -1

        
        if self.y < 0  or self.y > constants.SCREEN_HEIGHT:
            self.vel[1] *= -1            

            
        for e in Entity.entities:
            if e == self:
                continue

            intersection_rect = self.get_intersection_rect(e)
            
            if intersection_rect:
                if intersection_rect:                                        
                    tx = abs(intersection_rect[0]) / abs(self.vel[0])
                    ty = abs(intersection_rect[1]) / abs(self.vel[1])

                    if tx < ty:
                        self.x += -self.vel[0] * tx
                        self.y += -self.vel[1] * tx
                    else:
                        self.x += -self.vel[0] * ty
                        self.y += -self.vel[1] * ty
                    
                    if e == self.player:

                        angle_v = math_helper.inverse_lerp(
                            self.x,
                            e.x - e.width*0.5,
                            e.x + e.width*0.5)

                        new_angle = math_helper.lerp(
                            angle_v,
                            MIN_ANGLE,
                            math.pi - MIN_ANGLE)
                        
                        if intersection_rect[1] > intersection_rect[0]:
                            sign = math_helper.sign(self.vel[0])
                        else:
                            sign = math_helper.sign(self.vel[1])
                            
                        if sign > 0:
                            new_angle *= -1

                        new_vel = math_helper.rotate_vector(
                            [-BALL_VELOCITY,0],
                            new_angle)

                        self.vel = new_vel
                    else:
                        if (self.y >= e.y + self.height/2.0 + e.height/2.0 or
                            self.y <= e.y - self.height/2.0 - e.height/2.0):

                            self.vel[1] *= -1
                        else:
                            self.vel[0] *= -1

                        self.score_manager.score()                        
                        e.kill()
