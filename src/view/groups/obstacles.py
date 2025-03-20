import random
import pygame
from model.config import *
from view.sprites.scrolling import SpriteScrolling
from model.assets import *
from view.sprites.pterodactyl import Pterodactyl
import model.game


class Obstacles(pygame.sprite.Group):
    """
    Spawns objects that the dino must avoid.
    """
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.spawn_timer = 0
        self.spawn_rate = OBSTACLE_SPAWN_RATE
    

    def update(self, *args, **kwargs):
        self.spawn_obstacles()
        self.check_collision()


    def spawn_obstacles(self):
        self.spawn_timer += 1
        if self.spawn_timer > self.spawn_rate:
            self.spawn_timer = 0 
            self.spawn_rate = OBSTACLE_SPAWN_RATE + random.choice([1, -1]) * OBSTACLE_SPAWN_VARIANCE * random.random()
            if model.game.game_score >= PTERODACTYL_SPAWN_AT_SCORE and random.random() < PTERODACTYL_SPAWN_PROBABILITY:
                self.spawn_pterodactyl()
            else:
                self.spawn_cacti()


    def spawn_cacti(self):
            count = random.randint(1, CACTI_CLUSTER_MAX)
            x = GAME_WIDTH
            w = 0
            for _ in range(count):  
                spacing = random.randint(CACTI_SPACING_MIN, CACTI_SPACING_MAX)
                o = SpriteScrolling(
                    images=assets['images/cacti'],
                    x=x,
                    y=GAME_GROUND_Y,
                    speed_multiplier=1.0,
                    useMask=True
                )
                w += o.rect.width + spacing
                if w > CACTI_WIDTH_MAX:
                    break
                self.add(o)
                pygame.event.post(
                    pygame.event.Event(GAME_EVENT_TYPES.SPAWNED.value,
                    object=o,
                    layer=SCREEN_LAYERS.OBSTACLES.value)
                )
                x = o.rect.right + spacing


    def spawn_pterodactyl(self):
            o = Pterodactyl(
                x=GAME_WIDTH,
                y=random.randint(PTERODACTYL_MIN_Y, PTERODACTYL_MAX_Y)
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