import tkinter as tk
from game_class import Game
import asyncio
from websockets.sync.client import connect
import json 


W = 1024
H = 720
circle_radius = 25
circle_width = 8
offset = 40
symbol_radius = 70

# συντεταγμένες κέντρων κουτιών
symbol_position = [
    (0.26, 0.235),
    (0.5, 0.235),
    (0.74, 0.235),
    (0.26, 0.5),
    (0.5, 0.5),
    (0.74, 0.5),
    (0.26, 0.765),
    (0.5, 0.765),
    (0.74, 0.765),
]

def request_state():
    with connect("ws://reborn:9999") as websocket:
        websocket.send("state")
        message = websocket.recv()
        camera_board = json.loads(message)
    return camera_board
        # print(f"Received: {message}")

def get_new_position():
    camera_board = request_state()

    for i in range(9):
        if game.board[i] != camera_board[i]:
            change_point = i
            symbol = camera_board[i]
            return change_point, symbol
        
def update(evt=None):
    pos, s = get_new_position()
    place_symbol(pos, s)
    game.board[pos] = s

# συνάρτηση κύκλων
def create_circle(canvas, x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

window = tk.Tk() 
window.geometry(f"{W}x{H}")

canvas = tk.Canvas(window, width=W, height=H)
canvas.pack(fill = tk.BOTH, expand=True)
canvas.config(bg="white")

# πάνω αριστερά κύκλος
create_circle(canvas, 0+offset, 0+offset, circle_radius, outline='black', width=circle_width)
# πάνω δεξιά κύκλος
create_circle(canvas, W-offset, 0+offset, circle_radius, outline='black', width=circle_width)
# κάτω αριστερά κύκλος
create_circle(canvas, 0+offset, H-offset, circle_radius, outline='black', width=circle_width)
# κάτω δεξιά κύκλος
create_circle(canvas, W-offset, H-offset, circle_radius, outline='black', width=circle_width)

canvas.create_line(0.37*W, 0.10*H, 0.37*W, 0.90*H, width=circle_width)
canvas.create_line(0.63*W, 0.10*H, 0.63*W, 0.90*H, width=circle_width)
canvas.create_line(0.15*W, 0.37*H, 0.85*W, 0.37*H, width=circle_width)
canvas.create_line(0.15*W, 0.63*H, 0.85*W, 0.63*H, width=circle_width)

# ζωγράφισε Χ
def draw_X(x, y):
    canvas.create_line(x-symbol_radius, y-symbol_radius, x+symbol_radius, y+symbol_radius, fill='red', width=10, tag='S')
    canvas.create_line(x-symbol_radius, y+symbol_radius, x+symbol_radius, y-symbol_radius, fill='red', width=10, tag='S')
# ζωγράδισε O
def draw_O(x, y):
    create_circle(canvas, x, y, symbol_radius, outline='blue', width=10, tag='S')


def place_symbol(pos, symbol):
    if pos < 0 or pos > 8:
        return
    
    x, y = symbol_position[pos]
    x = x * W
    y = y * H
    if symbol == Game.X:
        draw_X(x, y)
    elif symbol == Game.O:
        draw_O(x, y)

def render():
    canvas.delete('S')

    for i, symbol in enumerate(game.board):
        place_symbol(i, symbol)


game = Game()
def on_reset(evt=None):
    global game
    game = Game()
    render()

def on_space(evt=None):
    game.ai_play()
    game.next_player()
    render()
    

# σχεδίασε σύμβολα
# for i in range(9):
# for position in symbol_position:
#     # print(position)
#     x, y = position
#     draw_X(x*W, y*H)
#     draw_O(x*W, y*H)

# place_symbol(0, 'X')
# place_symbol(1, 'O')


window.bind('<space>', on_space)
window.bind('<Return>', on_reset)
window.bind('c', update)

window.mainloop()
