import pygame
from enum import Enum, auto
from model.config import *
import model.assets



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
        ``alignment`` (ALIGNMENT_HORIZONTAL, optional): The horizontal alignment of the message lines, relative to ``x``. Defaults to ALIGNMENT_HORIZONTAL.CENTER.
    """
    def __init__(self, alignment=ALIGNMENT_HORIZONTAL.CENTER):
        super().__init__()
        self.font = pygame.font.Font(model.assets.assets["fonts/PressStart2P/regular"], FONT_SIZE)
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
            image = self.font.render(line, False, COLOR_FOREGROUND)
            images.append(image)
        height = sum(image.get_height() + MESSAGE_LINE_SPACING for image in images) - MESSAGE_LINE_SPACING
        width = max(image.get_width() for image in images)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0,0,0,0))  # Transparent background
        y = 0
        for image in images:
            self.image.blit(image, (0, y))
            y += image.get_height() + MESSAGE_LINE_SPACING
        match self.alignment:
            case ALIGNMENT_HORIZONTAL.LEFT:
                self.rect = self.image.get_rect(left=(MESSAGE_X, MESSAGE_Y))
            case ALIGNMENT_HORIZONTAL.RIGHT:
                self.rect = self.image.get_rect(right=(MESSAGE_X, MESSAGE_Y))
            case ALIGNMENT_HORIZONTAL.CENTER:
                self.rect = self.image.get_rect(center=(MESSAGE_X, MESSAGE_Y))
