import pygame
from typing import Tuple
from pathlib import Path

assets = {}  # Single dictionary for all assets

# # Initialize pygame if not already initialized
# if not pygame.get_init():
#     pygame.init()

# # Set up display if not already set
# if not pygame.display.get_init():
#     _ = pygame.display.set_mode((1, 1), pygame.NOFRAME)

# # Initialize pygame mixer for sounds
# if not pygame.mixer.get_init():
#     pygame.mixer.init()
        

def load_assets(asset_dir):
    for directory in Path(asset_dir).rglob("*"):
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
        rel_path = str(directory.relative_to(asset_dir))
        
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
