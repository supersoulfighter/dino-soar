import pygame

class MessageView(pygame.sprite.Sprite):
    """
    *A sprite that displays a message.*

    Use the ``message`` property to set the message. 
    Automatically splits a multiline message into multiple images because 
    ``pygame.font.Font`` does not support multiline strings.

    Parameters
    ----------
        ``x`` (int): The x-coordinate of the sprite.
        ``y`` (int): The y-coordinate of the sprite.
        ``lineHeight`` (int): The line height of the sprite.
        ``color`` (tuple): The color of the sprite.
        ``font`` (pygame.Font, optional): The font to use for the sprite.
        Defaults to None.
    """
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
