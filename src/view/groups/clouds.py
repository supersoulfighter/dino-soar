import random
import pygame
from model.config import *
from view.sprites.scrolling import SpriteScrolling
from model.assets import assets


class Clouds(pygame.sprite.Group):
    """
    Spawns clouds as SpriteScrolling objects
    """
    def __init__(self, speed_multiplier, spawn_chance, min_y, max_y):
        super().__init__()
        self.speed_multiplier = speed_multiplier
        self.spawn_chance = spawn_chance
        self.min_y = min_y
        self.max_y = max_y
    

    def update(self, *args, **kwargs):
        self.spawn()
    

    def spawn(self):
        if random.random() < self.spawn_chance:
            cloud = SpriteScrolling(
                images=assets['images/cloud'],
                x=GAME_WIDTH,
                y=random.randint(self.min_y, self.max_y),
                speed_multiplier=self.speed_multiplier,
                useMask=False
            )
            self.add(cloud)
            pygame.event.post(
                pygame.event.Event(GAME_EVENT_TYPES.SPAWNED.value,
                object=cloud,
                layer=SCREEN_LAYERS.GROUND.value)
            )