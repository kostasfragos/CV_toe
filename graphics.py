import tkinter as tk

W = 1024
H = 720
circle_radius = 25
circle_width = 8
offset = 40
symbol_radius = 70

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
    canvas.create_line(x-symbol_radius, y-symbol_radius, x+symbol_radius, y+symbol_radius, fill='red', width=10)
    canvas.create_line(x-symbol_radius, y+symbol_radius, x+symbol_radius, y-symbol_radius, fill='red', width=10)
# ζωγράδισε O
def draw_O(x, y):
    create_circle(canvas, x, y, symbol_radius, outline='blue', width=10)
    
draw_X(0.26*W, 0.5*H)
draw_O(0.74*W, 0.235*H)


window.mainloop()

