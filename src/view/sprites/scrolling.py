from view.sprites.base import SpriteBase
from model.game import game_speed



class SpriteScrolling(SpriteBase):
    def __init__(self, images, x, y, speed_multiplier=1.0, useMask=False, *groups):
        super().__init__(images=images, x=x, y=y, useMask=useMask, *groups)
        self.speed_multiplier = speed_multiplier


    def update(self):
        self.move()
 

    def move(self):
        self.rect.x -= game_speed * self.speed_multiplier
        if self.rect.right < 0:
            self.kill()  # Remove from all groups
