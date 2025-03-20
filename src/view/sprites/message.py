import pygame
from enum import Enum, auto

class ALIGNMENT_HORIZONTAL(Enum):
    LEFT = auto()
    RIGHT = auto()
    CENTER = auto()

class Message(pygame.sprite.Sprite):
    """
    Message
    =======
    *A sprite that displays a message.*

    Use the ``message`` property to set the message. Automatically splits a multiline message into multiple images because ``pygame.font.Font`` does not support multiline strings.

    Parameters
    ----------
        ``x`` (int): The x-coordinate of the message.
        ``y`` (int): The y-coordinate of the message.
        ``lineSpacing`` (int): Spacing between lines of text.
        ``color`` (tuple): The color of the message.
        ``font`` (pygame.Font, optional): The font to use for the message.Defaults to None.
        ``alignment`` (ALIGNMENT_HORIZONTAL, optional): The horizontal alignment of the message lines, relative to ``x``. Defaults to ALIGNMENT_HORIZONTAL.CENTER.
    """
    def __init__(self, x, y, lineSpacing, color, font=None, alignment=ALIGNMENT_HORIZONTAL.CENTER):
        super().__init__()
        self.x = x
        self.y = y
        self.lineSpacing = lineSpacing
        self.color = color
        self.font = font
        self._message = None
        self.message = ""
        self.alignment = alignment

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
        height = sum(image.get_height() + self.lineSpacing for image in images) - self.lineSpacing
        width = max(image.get_width() for image in images)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0,0,0,0))  # Transparent background
        y = 0
        for image in images:
            self.image.blit(image, (0, y))
            y += image.get_height() + self.lineSpacing
        match self.alignment:
            case ALIGNMENT_HORIZONTAL.LEFT:
                self.rect = self.image.get_rect(left=(self.x, self.y))
            case ALIGNMENT_HORIZONTAL.RIGHT:
                self.rect = self.image.get_rect(right=(self.x, self.y))
            case ALIGNMENT_HORIZONTAL.CENTER:
                self.rect = self.image.get_rect(center=(self.x, self.y))
