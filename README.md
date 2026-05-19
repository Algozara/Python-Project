# Snake — Mod the Game: Python Remix

A collaborative student project modifying a Python Snake game made with `tkinter`. This project documents code exploration, collaborative development, and the changes made to the tutorial version of the game for a class final project.

## Project Overview

This project started from the ImKennyYip tutorial implementation, **Code Snake Game in Python**, and the source repository [ImKennyYip/snake-python](https://github.com/ImKennyYip/snake-python). We modified the base game to add gameplay and usability improvements, a few visual changes, and documentation.

- **Visual Change:** Adjusted tile size and kept a simple color layout for the snake and food.
- **Gameplay Change:** Added `SPACE` to restart after Game Over and kept movement responsive with arrow keys.
- **Code Refactor:** Added docstrings, a `reset_game()` function, and cleaner organization in the script.

## Team Members & Roles

| Name | Role | Responsibility |
|------|------|----------------|
| Alexander Gonzalez | Team Lead | Game setup, code refactor, README, final submission |
| Alex | Developer 1 | Visual modifications and documentation |
| Ale | Developer 2 | Gameplay modifications and documentation |

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- No extra packages required for the base game
- Optional: `pygame` if background music or sound effects are added later

### Steps to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Algozara/Python-Project.git
   cd Python-Project
   ```

2. Run the game:
   ```bash
   python Snake_Game.py
   ```

## How to Play

- `↑` Arrow: Move Up
- `↓` Arrow: Move Down
- `←` Arrow: Move Left
- `→` Arrow: Move Right
- `SPACE`: Restart after Game Over

## Project Changes

### 1. Visual Change — Alex
**What was changed:**
- Adjusted the tile size to 25px and kept the game visually clean with red food and green snake tiles.

**File(s) modified:**
- `Snake_Game.py`

**How to see it:**
- Run the game and notice the larger grid tiles and simple color layout.

**Code snippet:**
```python
TILE_SIZE = 25
canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")
canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="green")
```

---

### 2. Gameplay Change — Ale
**What was changed:**
- Added `SPACE` bar restart using a new `reset_game()` function.
- Kept arrow key movement responsive using key press input.

**File(s) modified:**
- `Snake_Game.py`

**How to see it:**
- Play until Game Over, then press `SPACE` to restart the game without closing the window.

**Code snippet:**
```python
def reset_game():
    global snake, food, snake_body, velocityX, velocityY, game_over, score
    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
    food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
    snake_body = []
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0
```

---

### 3. Code Refactor — Alexander Gonzalez
**What was changed:**
- Added docstrings to the main functions.
- Cleaned up code structure and separated game reset logic into its own function.
- Improved readability for grading and future edits.

**File(s) modified:**
- `Snake_Game.py`

**Why this helps:**
- The code is easier to read, easier to debug, and easier to explain in the presentation.

## File Structure

```text
Python-Project/
├── Snake_Game.py     # Main game file
├── README.md         # This file
├── timeline.csv      # Project timeline
└── assets/           # Future images and sounds
```

## Testing

To verify everything works:

1. Run the game with `python Snake_Game.py`
2. Use the arrow keys to move the snake
3. Eat food and confirm the score increases
4. Crash into a wall or yourself and confirm Game Over appears
5. Press `SPACE` after Game Over to restart the game

## Original Game Source

- **Original project:** [ImKennyYip/snake-python](https://github.com/ImKennyYip/snake-python)
- **Tutorial video:** [Code Snake Game in Python - YouTube](https://www.youtube.com/watch?v=FtqWCo1_I4g)
- **Attribution:** This project is based on the original Snake tutorial by ImKennyYip

## Technical Details

- **Language:** Python 3.x
- **Library:** `tkinter` and `random`
- **Grid Size:** 25 x 25 tiles
- **Tile Size:** 25px
- **Window Size:** 625 x 625 px
- **Frame Rate:** 10 FPS

## How to Present This Project

- **Team Lead:** Introduces the project and explains the refactor
- **Developer 1:** Demonstrates the visual change
- **Developer 2:** Demonstrates the gameplay change

## Learning Outcomes Achieved

- Navigated and understood a Python codebase
- Made observable changes to the game
- Collaborated using GitHub and team roles
- Documented code and project changes clearly

## Stretch Goals (Optional)

- Add background music
- Add sound effects when food is eaten
- Add a high score system
- Replace rectangles with sprites later

## Troubleshooting

**Game won't start:**
- Make sure Python 3.8+ is installed
- Run `python --version` to check

**Snake won't move:**
- Click the game window first
- Use the arrow keys, not WASD

**Restart doesn't work:**
- Make sure `SPACE` is pressed after Game Over
- Confirm the `reset_game()` function is included in the script

## Contributing

This is a class project, but future improvements could be made by:
1. Forking the repo
2. Creating a branch
3. Making changes
4. Committing and pushing to GitHub
5. Opening a pull request

## Acknowledgments

- ImKennyYip for the tutorial and original idea
- Bates Technical College
- Instructor Joseph Kauer
- Python community

---

**Project Submission Date:** June 5, 2026  
