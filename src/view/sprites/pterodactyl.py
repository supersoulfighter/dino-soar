import pygame
from enum import Enum, auto
from typing import override
from model.assets import *
from view.sprites.scrolling import SpriteScrolling
from view.sprites.animating import SpriteAnimating
from model.config import *


class PterodactylStates(Enum):
    FLYING = auto()


class Pterodactyl(SpriteAnimating, SpriteScrolling):
    """
    A sprite that represents a pterodactyl obstacle in the game.
    
    Combines animation and scrolling behavior.
    """
    def __init__(self, x, y):
        super().__init__(
            images={PterodactylStates.FLYING: assets['images/pterodactyl']},
            animation_speed=PTERODACTYL_ANIMATION_SPEED,
            state_start=PterodactylStates.FLYING,
            x=x,
            y=y,
            speed_multiplier=PTERODACTYL_SPEED_MULTIPLIER,
            useMask=True
        )

    @override
    def update(self):
        super().update()  # Update animation
        self.move()  # Update position