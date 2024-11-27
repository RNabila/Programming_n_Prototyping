'''
Nabila Raisa, 01 and 02, 11/26/2024
CFU#14
'''

import simplegui 

def draw_handler(canvas):
    # Left Eye
    canvas.draw_line([50, 70], [50, 80], 2, "blue")  # Vertical line
    canvas.draw_line([50, 70], [60, 70], 2, "blue")  # Top horizontal line
    canvas.draw_line([60, 70], [60, 80], 2, "blue")  # Vertical line
    canvas.draw_line([60, 80], [50, 80], 2, "blue")  # Bottom horizontal line

    # Right Eye
    canvas.draw_line([140, 70], [140, 80], 2, "blue")  # Vertical line
    canvas.draw_line([140, 70], [150, 70], 2, "blue")  # Top horizontal line
    canvas.draw_line([150, 70], [150, 80], 2, "blue")  # Vertical line
    canvas.draw_line([150, 80], [140, 80], 2, "blue")  # Bottom horizontal line

    # Smile
    canvas.draw_line([70, 130], [80, 140], 2, "red")  # Left slant
    canvas.draw_line([80, 140], [90, 143], 2, "red")  # Middle curve
    canvas.draw_line([90, 143], [100, 140], 2, "red")  # Right slant

# Create frame
frame = simplegui.create_frame("CFU14 Happy Lines", 200, 200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)

# Start frame
frame.start()
