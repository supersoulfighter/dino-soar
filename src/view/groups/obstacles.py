import random
import pygame
from model.config import *
from view.sprites.scrolling import SpriteScrolling
from model.assets import *



class Obstacles(pygame.sprite.Group):
    def __init__(self, x, y, player):
        super().__init__()
        self.x = x
        self.y = y
        self.spawn_timer = 0
        self.player = player
    

    def update(self, *args, **kwargs):
        self.spawn()
        self.check_collision()
    

    def spawn(self):
        self.spawn_timer += 1
        if self.spawn_timer > 50 and random.random() < 0.03:
            self.spawn_timer = 0
            o = SpriteScrolling(
                images=assets['images/cacti'],
                x=self.x,
                y=self.y,
                speed_multiplier=1.0,
                useMask=True
            )
            self.add(o)
            pygame.event.post(
                pygame.event.Event(GAME_EVENT_TYPES.SPAWNED.value,
                object=o,
                layer=SCREEN_LAYERS.OBSTACLES.value)
            )


    def check_collision(self):
        # This could be more efficient by checking only obstacles that are close to the dino
        if pygame.sprite.spritecollideany(self.player, self, pygame.sprite.collide_mask):
            pygame.event.post(pygame.event.Event(GAME_EVENT_TYPES.CRASH.value))