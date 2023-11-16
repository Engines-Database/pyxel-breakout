import pyxel
import player
import constants
import brick
import ball
import score

from entity import Entity


class App():
    player = None
    ball = None
    
    finished = False

    
    def __init__(self):
        pyxel.init(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        pyxel.load("game.pyxres")

        self.score_manager = score.ScoreManager()
        self.reset()
        
        pyxel.run(self.update, self.draw)


    def reset(self):
        pyxel.playm(0, loop=True)
        
        self.finished = False

        self.player = None
        self.ball = None
        Entity.entities = [] # we trust python GC in this house
        
        self.score_manager.current_score = 0

        self.player = player.Player(
            constants.SCREEN_WIDTH * 0.5,
            constants.SCREEN_HEIGHT - 20
        )
        
        self.ball = ball.Ball(10, 80, self.player, self.score_manager)

        for x in range(constants.BRICKS_COLUMNS):
            for y in range(constants.BRICKS_LINES):
                b = brick.Brick(8 + (x*16),10+(y*6))
        
        
    def update(self):
        if not self.finished:
            for e in Entity.entities:
                e.update()
            self.score_manager.update()

            if len(Entity.entities) == 2: # only ball and paddle left
                self.finished = True
                self.score_manager.elapse_bonus()
        else:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.reset()


    def draw(self):
        pyxel.cls(0)
        for e in Entity.entities:
            e.draw()
        self.score_manager.draw()

        if self.finished:
            pyxel.text(35, 60, "Press space to restart", 3)

App()

