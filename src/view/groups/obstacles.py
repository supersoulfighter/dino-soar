import random
import pygame
from model.config import *
from view.sprites.scrolling import SpriteScrolling
from model.assets import *



class Obstacles(pygame.sprite.Group):
    """
    Spawns objects that the dino must avoid.
    """
    def __init__(self, x, y, player):
        super().__init__()
        self.x = x
        self.y = y
        self.player = player
        self.spawn_cacti_timer = 0
    

    def update(self, *args, **kwargs):
        self.spawn()
        self.check_collision()
    

    def spawn(self):
        self.spawn_cacti_timer += 1
        if self.spawn_cacti_timer > CACTI_SPAWN_RATE and random.random() < CACTI_SPAWN_VARIANCE:
            self.spawn_cacti_timer = 0  
            count = random.randint(1, CACTI_CLUSTER_MAX)
            x = self.x
            w = 0
            for _ in range(count):  
                spacing = random.randint(CACTI_SPACING_MIN, CACTI_SPACING_MAX)
                o = SpriteScrolling(
                    images=assets['images/cacti'],
                    x=x,
                    y=self.y,
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


    def check_collision(self):
        # This could be more efficient by checking only obstacles that are close to the dino
        if pygame.sprite.spritecollideany(self.player, self, pygame.sprite.collide_mask):
            pygame.event.post(pygame.event.Event(GAME_EVENT_TYPES.CRASH.value))