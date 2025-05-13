from typing import override
import model.assets
from view.sprites.animating import SpriteAnimating
from model.config import *



class DinoStates(Enum):
    RUNNING = auto()
    JUMPING = auto()
    DUCKING = auto()
    CRASHED = auto()



class Dino(SpriteAnimating):
    """
    Dino
    ====
    *A sprite that represents the player in the game.*

    """
    def __init__(self):
        super().__init__(
            images={
                DinoStates.RUNNING: model.assets.assets["images/dino/run"],
                DinoStates.JUMPING: model.assets.assets["images/dino/idle"],
                DinoStates.DUCKING: model.assets.assets["images/dino/duck"],
                DinoStates.CRASHED: model.assets.assets["images/dino/crash"]
            },
            animation_speed=DINO_ANIMATION_SPEED,
            state_start=DinoStates.RUNNING,
            x=DINO_START_X,
            y=DINO_START_Y,
            use_mask=True
        )
        self.ground_y = GROUND_Y
        self.jump_speed = DINO_JUMP_SPEED
        self.gravity = DINO_GRAVITY
        self.velocity = 0


    def jump(self):
        if self.state == DinoStates.RUNNING:
            self.velocity = self.jump_speed
            self.state = DinoStates.JUMPING
            model.assets.assets["sounds/dino/jump"].play()

    def duck(self, duck):
        if duck and self.state == DinoStates.RUNNING:
            self.state = DinoStates.DUCKING
        elif not duck and self.state == DinoStates.DUCKING:
            self.state = DinoStates.RUNNING

    @override
    def update(self):
        self.animate()
        self.move()
    
    def move(self):
        if self.state == DinoStates.JUMPING:
            self.rect.y += self.velocity
            self.velocity += self.gravity
            if self.rect.bottom >= self.ground_y:
                self.rect.bottom = self.ground_y
                self.velocity = 0
                self.state = DinoStates.RUNNING