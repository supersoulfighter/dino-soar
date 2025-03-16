import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, y, speed, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.bottom = y
        self.speed = speed
        # Create a second ground piece for seamless scrolling
        self.x2 = self.rect.width

    def update(self):
        # Move both ground pieces to the left
        self.rect.x -= self.speed
        self.x2 -= self.speed

        # Reset positions when ground moves off screen
        if self.rect.right <= 0:
            self.rect.left = self.x2 + self.rect.width
        if self.x2 + self.rect.width <= 0:
            self.x2 = self.rect.right

    def draw(self, screen):
        # Draw both ground pieces
        screen.blit(self.image, self.rect)
        screen.blit(self.image, (self.x2, self.rect.y))
