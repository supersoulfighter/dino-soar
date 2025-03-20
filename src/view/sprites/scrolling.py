from view.sprites.base import SpriteBase
import model.game



class SpriteScrolling(SpriteBase):
    """
    *A sprite that scrolls across the screen.*

    Parameters
    ----------
        ``images`` (Sequence or Surface): A sequence of images or a single image.
        ``x`` (int): The x-coordinate of the sprite.
        ``y`` (int): The y-coordinate of the sprite.
        ``speed_multiplier`` (float, optional): The speed multiplier for the sprite.
        Defaults to 1.0.
        ``useMask`` (bool, optional): Whether to create a collision mask for the sprite.
        Defaults to False.
    """
    def __init__(self, images, x, y, speed_multiplier=1.0, useMask=False, *groups):
        super().__init__(images=images, x=x, y=y, useMask=useMask, *groups)
        self.speed_multiplier = speed_multiplier


    def update(self):
        self.move()
 

    def move(self):
        self.rect.x -= model.game.game_speed * self.speed_multiplier
        if self.rect.right < 0:
            self.kill()  # Remove from all groups
