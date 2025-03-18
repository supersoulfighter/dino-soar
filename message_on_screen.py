import pygame

class MessageOnScreen(pygame.sprite.Sprite):
    def __init__(self, x, y, lineHeight, color, font=None):
        super().__init__()
        self.x = x
        self.y = y
        self.lineHeight = lineHeight
        self.color = color
        self.font = font
        self._message = None
        self.message = ""

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if value == self._message:
            return
        if not value:
            self.image = pygame.Surface((0, 0))
            self.rect = pygame.Rect(0, 0, 0, 0)
            self._message = value
            return

        self._message = value

        lines = value.split('\n')
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
        self.rect = self.image.get_rect(center=(self.x, self.y))
