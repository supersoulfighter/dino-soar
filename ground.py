import pygame

class Ground(pygame.sprite.Group):
    def __init__(self, y, speed, image):
        super().__init__()
        self.A = pygame.sprite.Sprite(self)
        self.B = pygame.sprite.Sprite(self)
        self.add([self.A, self.B])
        self.A.image = self.B.image = image
        self.A.rect = image.get_rect()
        self.B.rect = image.get_rect()
        self.A.rect.bottom = self.B.rect.bottom = y
        self.A.rect.x = 0
        self.B.rect.x = self.A.rect.width
        self.speed = speed


    def update(self, *args, **kwargs):
        # Move both ground pieces to the left
        self.A.rect.x -= self.speed
        self.B.rect.x -= self.speed

        # Reset positions when ground moves off screen
        if self.A.rect.right <= 0:
            self.A.rect.left = self.B.rect.right
        elif self.B.rect.right <= 0:
            self.B.rect.left = self.A.rect.right
