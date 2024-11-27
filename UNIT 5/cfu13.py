'''
Nabila Raisa, 01 and 02, 11/26/2024
CFU#13
'''

import simplegui 

def draw_handler(canvas):
    # Left Eye
    canvas.draw_point([50, 70], "blue")
    canvas.draw_point([50, 72], "blue")
    canvas.draw_point([50, 74], "blue")
    canvas.draw_point([50, 76], "blue")
    canvas.draw_point([50, 78], "blue")
    canvas.draw_point([52, 70], "blue")
    canvas.draw_point([54, 70], "blue")
    canvas.draw_point([56, 70], "blue")
    canvas.draw_point([56, 72], "blue")
    canvas.draw_point([56, 74], "blue")
    canvas.draw_point([56, 76], "blue")
    canvas.draw_point([56, 78], "blue")
    canvas.draw_point([54, 78], "blue")
    canvas.draw_point([52, 78], "blue")
    
    # Right Eye
    canvas.draw_point([140, 70], "blue")
    canvas.draw_point([140, 72], "blue")
    canvas.draw_point([140, 74], "blue")
    canvas.draw_point([140, 76], "blue")
    canvas.draw_point([140, 78], "blue")
    canvas.draw_point([142, 70], "blue")
    canvas.draw_point([144, 70], "blue")
    canvas.draw_point([146, 70], "blue")
    canvas.draw_point([146, 72], "blue")
    canvas.draw_point([146, 74], "blue")
    canvas.draw_point([146, 76], "blue")
    canvas.draw_point([146, 78], "blue")
    canvas.draw_point([144, 78], "blue")
    canvas.draw_point([142, 78], "blue")
    
    # Smile
    canvas.draw_point([70, 130], "red")
    canvas.draw_point([72, 132], "red")
    canvas.draw_point([74, 134], "red")
    canvas.draw_point([76, 135], "red")
    canvas.draw_point([78, 136], "red")
    canvas.draw_point([80, 137], "red")
    canvas.draw_point([82, 137], "red")
    canvas.draw_point([84, 137], "red")
    canvas.draw_point([86, 136], "red")
    canvas.draw_point([88, 135], "red")
    canvas.draw_point([90, 134], "red")
    canvas.draw_point([92, 132], "red")
    canvas.draw_point([94, 130], "red")
    
# Create frame
frame = simplegui.create_frame("CFU13 Happy Dots", 200, 200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)

# Start frame
frame.start()
