import random
import pygame
from model.config import *
from view.sprites.scrolling import SpriteScrolling
import model.assets


class Clouds(pygame.sprite.Group):
    """
    Clouds
    ======
    *Spawns clouds as ``SpriteScrolling`` objects.*
    """
    

    def update(self, *args, **kwargs):
        self.spawn()
    

    def spawn(self):
        if random.random() < CLOUD_SPAWN_CHANCE:
            cloud = SpriteScrolling(
                images=model.assets.assets['images/cloud'],
                x=GAME_WIDTH,
                y=random.randint(CLOUD_MIN_Y, CLOUD_MAX_Y),
                speed_multiplier=CLOUD_SPEED_MULTIPLIER,
                use_mask=False
            )
            self.add(cloud)
            pygame.event.post(
                pygame.event.Event(GAME_EVENT_TYPES.SPAWNED.value,
                                   object=cloud,
                                   layer=SCREEN_LAYERS.GROUND.value)
            )