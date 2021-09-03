"""
File: random_circles.py
-------------------
Draws 10 random circles such that each circle is on the screen.
"""

from graphics import Canvas
# this is needed to generate random numbers.  Don't delete this.
import random

# The number of circles to draw
NUM_CIRCLES = 10


def main():
    """
    You should write your code between the two lines written
    already that set up the canvas.
    You should replace this comment with a better, more descriptive one.
    """
    canvas = Canvas()
    canvas.set_canvas_title("Random Circles")
    width = canvas.get_canvas_width()
    height = canvas.get_canvas_height()
    for i in range(NUM_CIRCLES):
        radiant = random.randint(50, 200)
        x1 = random.randint(0,width - radiant)
        x2 = x1 + radiant
        y1 = random.randint(0,height - radiant)
        y2 = y1 + radiant
        oval = canvas.create_oval(x1,y1,x2,y2)
        color = canvas.get_random_color()
        canvas.set_fill_color(oval, color)
    canvas.mainloop()


# call the function
if __name__ == '__main__':
    main()
