import random
import pygame
from config import *
from cactus import Cactus
from assets import assets


class Obstacles(pygame.sprite.Group):
    def __init__(self, x, y, speed, player):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.spawn_timer = 0
        self.score = 0
        self.player = player
    

    def update(self, *args, **kwargs):
        self.spawn()
        self.check_collision()
    

    def spawn(self):
        self.spawn_timer += 1
        if self.spawn_timer > 50 and random.random() < 0.03:
            self.spawn_timer = 0
            o = Cactus(assets['images/cacti'], x=self.x, y=self.y, speed=self.speed)
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