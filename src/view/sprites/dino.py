from enum import Enum, auto
from typing import override
import model.assets
from view.sprites.animating import SpriteAnimating



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

    Parameters
    ----------
        ``animations`` (dict): A dictionary whose keys are the states and values are a ``Sequence`` of images. Or supply a single ``Surface``.
        ``animation_speed`` (float): The speed of the animation.
        ``state_start`` (str): The initial state of the sprite.
        ``x`` (int): The x-coordinate of the sprite.
        ``y`` (int): The y-coordinate of the sprite.
        ``ground_y`` (int): The y-coordinate of the ground.
        ``useMask`` (bool, optional): Whether to create a collision mask for the sprite. Defaults to False.
        ``jump_speed`` (float): The vertical speed of the jump.
        ``gravity`` (float): Downward acceleration on the jump.
    """
    def __init__(self, animations, animation_speed, state_start, x, y, ground_y, useMask, jump_speed, gravity):
        super().__init__(images=animations, animation_speed=animation_speed, state_start=state_start, x=x, y=y, useMask=useMask)
        self.ground_y = ground_y
        self.jump_speed = jump_speed
        self.gravity = gravity
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