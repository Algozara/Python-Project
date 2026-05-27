# Snake Game Project – Mod the Game: Python Remix

This is my version of the classic Snake game built in Python with `tkinter`.  
For my Python course final, I took the original tutorial code and added my own changes: a bottom status bar, color tweaks, SPACE restart, sound effects when you eat food, a saved best-score system, and a pause feature using the `P` key.

The goal of this project is to practice reading someone else’s code, making visible changes, and documenting what I did in a way that a teacher (or future employer) can follow.

---

## Where this started

This project is based on the ImKennyYip tutorial **“Code Snake Game in Python”** and his repo [ImKennyYip/snake-python](https://github.com/ImKennyYip/snake-python).  

I used his version as the starting point and then changed the game to:

- Look a little cleaner  
- Feel better to play  
- Track and save your best score  
- Give feedback when you eat food (sound + UI)  
- Let you pause and resume the game mid-run

## Team Members & Roles

| Name | Role | Responsibility |
|---|---|---|
| Alexander Gonzalez | Team Lead | Game setup, code changes, README updates, final submission |
| Alexander Gonzalez | Developer 1 | Visual changes and documentation |
| Alex Gonzalez | Developer 2 | Gameplay changes and documentation |

---

## What I changed

### 1. Visual tweaks + bottom panel

- Kept the grid size at 25 x 25 and tile size at 25px
- Snake uses a brighter **chartreuse** color
- Food uses **crimson** so it stands out on the black background
- Added a dark bottom bar under the game to show:
  - current score
  - best score (saved)
  - status messages like “Game Over! Press SPACE to restart.”

Example:

```python
TILE_SIZE = 25
PANEL_HEIGHT = 40

score_label = tkinter.Label(
    status_panel,
    text="Score: 0 | Best: 0",
    font=("Arial", 12, "bold"),
    fg="chartreuse",
    bg="#1a1a1a"
)
```

---

### 2. Gameplay change – SPACE restart

I added a clean restart flow so you don’t have to close and re-open the window every time you lose.

- Press `SPACE` **after Game Over** to reset everything:
  - snake position
  - body segments
  - direction
  - score
  - food position
- The bottom panel message changes to tell you when you can press SPACE.

Key pieces:

```python
def reset_game():
    global snake, food, snake_body, game_over, score, velocityX, velocityY, paused
    game_over = False
    score = 0
    paused = False
    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
    snake_body = []
    velocityX = 0
    velocityY = 0
    food.x = random.randint(0, COLS - 1) * TILE_SIZE
    food.y = random.randint(0, ROWS - 1) * TILE_SIZE
    score_label.config(text=f"Score: 0 | Best: {high_score}", fg="chartreuse")
    tip_label.config(text="Use Arrow Keys to move", fg="#888888")

def handle_space(event):
    if game_over:
        reset_game()

window.bind("<space>", handle_space)
```

---

### 3. Sound + best score system

I wanted the game to feel less “silent” and also show progress over multiple games.

- When the snake eats food, it plays a short beep using `winsound.Beep(...)`
- The game keeps track of `high_score`
- `high_score` is stored in a text file called `high_score.txt` so it sticks around next time you run the game

Code highlight:

```python
def load_high_score():
    global high_score
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0

def save_high_score():
    with open("high_score.txt", "w") as f:
        f.write(str(high_score))

def play_eat_sound():
    def _play():
        winsound.Beep(600, 80)
    threading.Thread(target=_play, daemon=True).start()
```

Then inside the collision with food:

```python
if snake.x == food.x and snake.y == food.y:
    snake_body.append(Tile(food.x, food.y))
    food.x = random.randint(0, COLS - 1) * TILE_SIZE
    food.y = random.randint(0, ROWS - 1) * TILE_SIZE
    score += 1
    play_eat_sound()
    if score > high_score:
        high_score = score
        save_high_score()
```

The bottom panel shows:

```python
score_label.config(text=f"Score: {score} | Best: {high_score}")
```

---

### 4. New feature – pause with `P`

I added a pause feature so you can stop the game without closing it.

- Press `P` to pause the game and stop the snake from moving
- Press `P` again to unpause and keep playing
- While paused, the bottom status text changes to: `"Paused - press P to resume"`
- You can’t pause on the Game Over screen (SPACE still handles restart there)

Key pieces:

```python
paused = False  # new flag

def handle_pause(event):
    global paused, game_over

    if game_over:
        return  # no pausing on game over

    paused = not paused  # toggle True/False

    if paused:
        tip_label.config(text="Paused - press P to resume", fg="#ffaa00")
    else:
        tip_label.config(text="Use Arrow Keys to move", fg="#888888")

def move():
    global snake, food, snake_body, game_over, score, high_score, paused
    if game_over or paused:
        return
    # ... rest of move logic ...

window.bind("p", handle_pause)
window.bind("P", handle_pause)
```

---

## How to run it

1. Make sure Python 3.8+ is installed.
2. Clone or download this repo:

```bash
git clone https://github.com/Algozara/Python-Project.git
cd Python-Project
```

3. Run the game:

```bash
python Snake_Game.py
```

This version uses `winsound`, which is built into Python on Windows. On other OSes, the sound may not work the same.

---

## Controls

- `↑` move up  
- `↓` move down  
- `←` move left  
- `→` move right  
- `SPACE` restart after Game Over  
- `P` pause / unpause during the game  

---

## File layout

```text
Python-Project/
├── Snake_Game.py      # Main game code (tkinter)
├── README.md          # Project notes (this file)
├── timeline.csv       # Project timeline for the class
└── high_score.txt     # Created after playing, stores best score
```

---

## What I got out of this

From this project I practiced:

- Working with an existing codebase instead of starting from scratch
- Using `tkinter` to build a small game UI
- Handling keyboard events for movement, restart, and pause
- Saving simple data to a file (`high_score.txt`)
- Keeping the window layout clean and centered
- Writing a README that explains what changed and how to run it

This is part of my Python work for Bates Technical College as I work toward my AAS in Cybersecurity and build projects I can show on GitHub and LinkedIn.

---

## Original source / credit

- Original tutorial project: [ImKennyYip/snake-python](https://github.com/ImKennyYip/snake-python) 
- YouTube tutorial: [Code Snake Game in Python](https://www.youtube.com/watch?v=FtqWCo1_I4g)  
- Instructor: Joseph Kauer – Bates Technical College
