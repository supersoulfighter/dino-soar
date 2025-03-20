# Dino Soar 🦖

A Python implementation of the Chrome browser's offline dinosaur runner game, built using Pygame.

## Description

Dino Soar is a partial clone of Chrome's famous no-network dinosaur game where players control a running dinosaur, jumping over cacti and ducking under pterodactyls to achieve the highest possible score.

## Features

- MVC (Model-View-Controller) architecture
- Frame-based animations and sprite-based graphics
- Progressive difficulty scaling
- Sound effects
- Keyboard controls for jump and duck actions

## Getting started

### Prerequisites

- Python 3.x
- Virtual environment (venv)

### Installation

1. Clone the repository
2. Set up the virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Game

From the project root directory:
```bash
python src/main.py
```

## Controls

- **Space/Up Arrow**: Jump
- **Down Arrow**: Duck

## Project Structure

```
dino-soar/
├── assets/           # Game assets (images, fonts, sounds)
├── src/             # Source code
│   ├── model/       # Game logic and state
│   ├── view/        # Visual components and sprites
│   └── main.py      # Main game controller
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Known differences from original

- No splash / intro screen
- No night mode
- No easter eggs / collectables
- No high score tracker
- No restart button
- No slow mode
- Score formula slightly different
- Cacti grouping slightly different
- Obstacle spawning logic slightly different
- Jump trajectory for dino slightly different
- Higher max speed
- Sounds are recorded, not synthesized?
- Not implemented for mobile device or other window sizes

## Author

Jeff Ettenhofer
