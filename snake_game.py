import tkinter
import random

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
score_label = tkinter.Label(status_panel, text="Score: 0", font=("Arial", 12, "bold"),fg="chartreuse", bg="#1a1a1a")
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


def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
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

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="chartreuse")

    if (game_over):
        canvas.create_text(WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2, font = "Arial, 20", text = f"Game Over: {score}", fill ="white")
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill="white")
        score_label.config(text=f"Final Score: {score}", fg="crimson")
        trip_label.config(text="Game Over!", fg="crimson")
    else:
        score_label.config(text=f"Score: {score}")

    window.after(100, draw) #100ms = 1/10 second, 10 frames per second

draw()
window.bind("<KeyRelease>", change_direction) #KeyRelease event is triggered when a key is released, and the change_direction function will be called with the event as an argument
window.mainloop()
