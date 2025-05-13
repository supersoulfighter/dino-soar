import pygame
from view.sprites.base import SpriteBase



class SpriteAnimating(SpriteBase):
    """
    SpriteAnimating
    ===============
    *A sprite that can do multiple animations.*

    Each animation is activated by setting the `state` property.
     
    Parameters
    ----------
        ``images`` (dict): A dictionary whose keys are the states and values are a ``Sequence`` of images. Or supply a single ``Surface``.
        ``animation_speed`` (float): The speed of the animation.
        ``state_start`` (str): The initial state of the sprite.
        ``x`` (int): The x-coordinate of the sprite.
        ``y`` (int): The y-coordinate of the sprite.
        ``useMask`` (bool, optional): Whether to create a collision mask for the sprite. Defaults to False.
        ``*groups`` (pygame.sprite.Group, optional): The groups to add the sprite to.
    """
    def __init__(self, images, animation_speed, state_start, x, y, use_mask=False, *groups, **kwargs):
        self.use_mask = use_mask
        self.animations = images
        self.animation_speed = animation_speed
        self._state = None
        self.state = state_start
        self.animate()
        super().__init__(images=images, x=x, y=y, use_mask=use_mask, *groups, **kwargs)



    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value == self._state:
            return
        self.state_previous = self._state
        self._state = value
        self.animation_time = 0
        self.animation_frame = 0
        self.animation_length = 0 if isinstance(self.animations[value], pygame.Surface) else len(self.animations[value])


    def update(self):
        self.animate()
        
        
    def animate(self):
        if self.animation_length > 0:
            self.animation_time += self.animation_speed
            if self.animation_time >= self.animation_length:
                self.animation_time = 0
            self.animation_frame = int(self.animation_time)
            self.image = self.animations[self.state][self.animation_frame]
        else:
            self.image = self.animations[self.state]
        # All animation frames should have the same size, so rect not updated
