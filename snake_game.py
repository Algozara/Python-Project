import tkinter
import random
import winsound
import threading

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOWS_WIDTH = TILE_SIZE * ROWS
WINDOWS_HEIGHT = TILE_SIZE * COLS
PANEL_HEIGHT = 40  # Bottom status panel height

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg= "black", width=WINDOWS_WIDTH, height=WINDOWS_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
# Bottom status panel
status_panel = tkinter.Frame(window, bg="#1a1a1a", width=WINDOWS_WIDTH, height=PANEL_HEIGHT)
status_panel.pack(fill="x")
status_panel.pack_propagate(False)
score_label = tkinter.Label(status_panel, text="Score: 0 | Best: 0", font=("Arial", 12, "bold"),fg="chartreuse", bg="#1a1a1a")
score_label.pack(side="left", padx=12, pady=8)

tip_label = tkinter.Label(status_panel, text="Use Arrow Keys to move",font=("Arial", 10), fg="#888888", bg="#1a1a1a")
tip_label.pack(side="right", padx=12, pady=8)
window.update()

#center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (WINDOWS_WIDTH / 2))
window_y = int((screen_height / 2) - ((WINDOWS_HEIGHT + PANEL_HEIGHT) / 2))
window.geometry(f"{WINDOWS_WIDTH}x{WINDOWS_HEIGHT + PANEL_HEIGHT}+{window_x}+{window_y}")

#initialize game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #single tile snake's head
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
velocityX = 0
velocityY = 0
snake_body = [] #multiple tile snake's body
game_over = False
score = 0
high_score = 0
paused = False

def load_high_score():
    global high_score
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0
    
load_high_score()

def save_high_score():
    with open("high_score.txt", "w") as f:
            f.write(str(high_score))

def play_eat_sound():
    def _play():
        winsound.Beep(600, 80)  # 600hz tone, 80ms
    threading.Thread(target=_play, daemon=True).start()

def reset_game():
    global snake, food, snake_body, game_over, score, velocityX, velocityY, paused

    # Reset main flags and score
    game_over = False
    score = 0
    paused = False

    # Reset snake head position
    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)

    # Clear and reset snake body
    snake_body = []

    # Reset movement direction (stopped)
    velocityX = 0
    velocityY = 0

    # Reset food position
    food.x = random.randint(0, COLS - 1) * TILE_SIZE
    food.y = random.randint(0, ROWS - 1) * TILE_SIZE

    # Reset bottom labels
    score_label.config(text=f"Score: 0 | Best: {high_score}", fg="chartreuse")
    tip_label.config(text="Use Arrow Keys to move", fg="#888888")


def change_direction(e): #e = event
    # print(e)
    # print(e.keysym)
    global velocityX, velocityY, game_over
    if game_over:
        return


    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def handle_space(event):
    # Only restart if the game is currently over
    if game_over:
        reset_game()

def handle_pause(event):
    global paused

    # Do not allow pausing if the game is over
    if game_over:
        return
    
    # Toggle the paused flag
    paused = not paused

    # Update the bottom label
    if paused:
        tip_label.config(text="Game Paused. Press 'P' to resume.", fg="yellow")
    else:
        tip_label.config(text="Use Arrow Keys to move", fg="#888888")

def move():
    global snake, food, snake_body, game_over, score, high_score, paused
    if game_over or paused:
        return
    
    if(snake.x <0 or snake.x >= WINDOWS_WIDTH or snake.y < 0 or snake.y >= WINDOWS_HEIGHT):
        game_over = True
        return
    
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return


    #collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y)) #add new tile to the snake's body
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1
        play_eat_sound()
        if score > high_score:
            high_score = score
            save_high_score()

    #update the snake's body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, score
    move()

    canvas.delete("all")

    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="crimson")

    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="chartreuse")

    #draw snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="chartreuse")

    if (game_over):
        canvas.create_text(WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2, font = "Arial, 20", text = f"Game Over: {score}", fill ="white")
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill="white")
        
        score_label.config(text=f"Final Score: {score} | Best: {high_score}", fg="crimson")
        tip_label.config(text="Game Over! Press SPACE to restart.", fg="crimson")
    else:
        score_label.config(text=f"Score: {score} | Best: {high_score}")

    window.after(100, draw) #100ms = 1/10 second, 10 frames per second

draw()
window.bind("<KeyPress>", change_direction) #KeyRelease event is triggered when a key is released, and the change_direction function will be called with the event as an argument
window.bind("<space>", handle_space)
window.bind("p", handle_pause)
window.bind("P", handle_pause)
window.mainloop()
