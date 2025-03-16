import pygame

class MessageOnScreen(pygame.sprite.Sprite):
    def __init__(self, x, y, lineHeight, color, font=None):
        super().__init__()
        self.x = x
        self.y = y
        self.lineHeight = lineHeight
        self.color = color
        self.font = font
        self.message = ""
        self.image = None

    def update(self):
        lines = self.message.split('\n')
        images = []
        for line in lines:
            image = self.font.render(line, False, self.color)
            images.append(image)
        height = sum(image.get_height() + self.lineHeight for image in images) - self.lineHeight
        width = max(image.get_width() for image in images)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0,0,0,0))  # Transparent background
        y = 0
        for image in images:
            self.image.blit(image, (0, y))
            y += image.get_height() + self.lineHeight

    def draw(self, screen):
        rect = self.image.get_rect()
        rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(self.image, rect)
