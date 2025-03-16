import pygame
import random
from cactus import Cactus
from assets import assets


class ObstacleGroup(pygame.sprite.Group):
    def __init__(self, x, y, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.spawn_timer = 0
        self.score = 0
    
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

       # Update spawn timer
        self.spawn_timer += 1
        
        # Try to spawn new obstacle
        if self.spawn_timer > 50 and random.random() < 0.03:
            self.spawn_timer = 0
            self.add(Cactus(assets['images/cacti'], x=self.x, y=self.y, speed=self.speed))
        
        # Remove offscreen obstacles and update score
        for obstacle in self.sprites():
            if obstacle.offscreen():
                obstacle.kill()  # Remove from all groups
    
    def draw(self, screen):
        for sprite in self.sprites():
            sprite.draw(screen)
    
    def check_collision(self, dino) -> bool:
        return pygame.sprite.spritecollideany(dino, self) is not None
