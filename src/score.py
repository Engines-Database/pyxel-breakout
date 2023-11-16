import pyxel

SCORE_FRAMES_TIMEOUT = 30


class ScoreManager():
    current_score = 0
    bonus_multiplier = 0
    bonus_score = 0

    elapsed_frames = 0

    
    def score(self):
        self.elapsed_frames = 0
        self.bonus_multiplier += 1
        self.bonus_score += self.bonus_multiplier * 10
    
    
    def update(self):
        self.elapsed_frames += 1

        if self.bonus_score > 0:
            if self.elapsed_frames > 30:
                self.elapse_bonus()


    def elapse_bonus(self):
        self.current_score += self.bonus_score
        self.bonus_multiplier = 0
        self.bonus_score = 0
    

    def draw(self):
        pyxel.text(1,1,f"Score: {self.current_score}",4)
        if self.bonus_score > 0:
            pyxel.text(60,1,f"{self.bonus_score} (x{self.bonus_multiplier})",5)
