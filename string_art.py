"""
File: string_art.py
-------------------
This program creates string art using only straight lines.
"""

from graphics import Canvas

# Size of the canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# The number of pixels between end points of each line
LINE_SPACING = 20

# The number of lines we will have to draw
NUM_LINES = CANVAS_WIDTH // LINE_SPACING


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("String Art")

    for i in range(NUM_LINES):
        canvas.create_line(0,i * LINE_SPACING,LINE_SPACING * (i + 1),CANVAS_HEIGHT)



    canvas.mainloop()


if __name__ == "__main__":
    main()
