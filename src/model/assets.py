"""
Asset loader
============
*This module makes working with assets (images, sounds, fonts) easier.*

The ``load_assets()`` function takes a root asset directory and recursively loads assets in subfolders.

- Images are converted to ``pygame.Surfaces``.
- Sounds to ``pygame.Sounds``.
- Fonts are left as ``Path`` references, because a ``pygame.Font`` must be created for each font size, so this module won't know what sizes are needed ahead of time.

If multiple assets are found in a folder, they are converted to a tuple. This makes it easier to have a set of animation frames, for example.

All assets are loaded into a single dictionary, the ``assets`` global variable. The keys are the paths to the assets, e.g., "images/player/jump".
"""
import pygame
from typing import Tuple
from pathlib import Path

# Single dictionary for all assets
assets = {}


def load_assets(assets_relative_path: str):
    """
    load_assets
    ===========

    *Load assets into the ``assets`` global variable.*

    Parameters
    ----------
        ``assets_relative_path``: This should be the root directory of all assets, relative to the project folder. For example, "./assets".
    """
    # This little hack is needed for PyCharm as it treats the root directory as the current directory.
    a = Path(assets_relative_path)
    if not a.exists():
        asset_relative_path = "../" + a.stem
        a = Path(assets_relative_path)

    for directory in a.rglob("*"):
        if not directory.is_dir():
            continue
            
        # Skip certain directories
        if any(skip in str(directory) for skip in ["__pycache__", ".git"]):
            continue
        
        # Get all files in this directory
        files = [f for f in directory.iterdir() if f.is_file()]
        if not files:
            continue
        
        # Group files by type
        images = [f for f in files if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']]
        sounds = [f for f in files if f.suffix.lower() in ['.wav', '.mp3', '.ogg']]
        fonts = [f for f in files if f.suffix.lower() in ['.ttf', '.otf']]
        
        # Create relative path key
        rel_path = str(directory.relative_to(assets_relative_path))
        
        # Load images
        if images:
            surfaces = tuple(pygame.image.load(str(img)).convert_alpha() for img in sorted(images))
            assets[rel_path] = surfaces[0] if len(surfaces) == 1 else surfaces
        
        # Load sounds
        if sounds:
            sound_effects = tuple(pygame.mixer.Sound(str(snd)) for snd in sorted(sounds))
            assets[rel_path] = sound_effects[0] if len(sound_effects) == 1 else sound_effects
        
        # Load fonts
        if fonts:
            assets[rel_path] = fonts[0] if len(fonts) == 1 else sorted(fonts)



def scale_image(image: pygame.Surface, scale: float) -> pygame.Surface:
    """Scale an image by a factor."""
    if scale == 1:
        return image
    new_size = (int(image.get_width() * scale), int(image.get_height() * scale))
    return pygame.transform.scale(image, new_size)

def scale_images(images: Tuple[pygame.Surface, ...], scale: float) -> Tuple[pygame.Surface, ...]:
    """Scale a tuple of images by a factor."""
    return tuple(scale_image(img, scale) for img in images)

def print_assets():
    """Print all loaded assets for debugging."""
    print("\nLoaded Assets:")
    for path, asset in assets.items():
        asset_type = "image(s)" if isinstance(asset, (pygame.Surface, tuple)) and isinstance(asset[0] if isinstance(asset, tuple) else asset, pygame.Surface) else \
                    "sound(s)" if isinstance(asset, (pygame.mixer.Sound, tuple)) and isinstance(asset[0] if isinstance(asset, tuple) else asset, pygame.mixer.Sound) else \
                    "font(s)"
        count = len(asset) if isinstance(asset, tuple) else 1
        print(f"  {path}: {count} {asset_type}")
