'''
Nabila Raisa, 01 and 02, CFU#15
Drawing Happy face with polygons only.
'''

import simplegui

def draw_handler(canvas):
    #canvas.draw_polygon([(x,y), (x2,y2), (x3,y3)], width, "color")
    #the face (square)
    canvas.draw_polygon([(50, 50), (150, 50), (150, 150), (50, 150)], 2, 'Black', 'Yellow')
    
    #left eye
    canvas.draw_polygon([(70,80),(80,80),(80,90), (70,90)], 2, "Black", "white")
    
    #right eye
    canvas.draw_polygon([(120, 80), (130, 80), (130, 90), (120, 90)], 2, "black", "white")
    
    #nose (this should be a rlly tiny triangle)
    canvas.draw_polygon([(95, 100), (105, 100), (100, 110)], 2, "black", "pink")
    
    #mouth (will b e using a triangle thats stretched)
    canvas.draw_polygon([(70, 120), (130, 120), (100, 140)], 2, "black", "white")
    
    

    
   
frame = simplegui.create_frame("CFU15 Happy Shapes", 200, 200)
frame.set_draw_handler(draw_handler)

frame.start()
