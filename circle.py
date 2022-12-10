from OpenGL.GL import *
import numpy as np
from map import *
# PACMAN CIRCLE


def drawCurve(radius, pos_x, pos_y):
    x = 0
    y = radius
    d = 1 - radius

    trasnlate = np.array([[1, 0, pos_x],
                          [0, 1, pos_y],
                          [0, 0, 1]])

    v1 = np.array([[0],  # center of circle
                  [0],
                  [1]])

    v11 = np.matmul(trasnlate, v1)  # translate center of circle

    while x < y:

        glColor3f(1.0, 1.0, 0.0)
        glPointSize(1)
        glBegin(GL_POINTS)

        # glVertex2f(pos + x1 + y, pos + y1 + x)      #zone-1
        glVertex2f(v11[0][0] + x, v11[1][0] + y)  # zone-2
        glVertex2f(v11[0][0] - x, v11[1][0] + y)  # zone-3
        glVertex2f(v11[0][0] - y, v11[1][0] + x)  # zone-4
        glVertex2f(v11[0][0] - y, v11[1][0] - x)  # zone-5
        glVertex2f(v11[0][0] - x, v11[1][0] - y)  # zone-6
        glVertex2f(v11[0][0] + x, v11[1][0] - y)  # zone-7
        # glVertex2f(pos + x1 + y, pos + y1 - x)      #zone-8

        glEnd()

        if d < 0:

            # choose east

            d = d + 2*x + 3
            x = x + 1

        else:
            # choosing south east

            d = d + 2*x - 2*y + 5
            x = x + 1
            y = y - 1

    # drawing the pacman mouth
    draw_midpoint_lines(v11[0][0] + x, v11[1][0] + y,
                        v11[0][0], v11[1][0], 'ok')
    draw_midpoint_lines(v11[0][0] + x, v11[1][0] + -
                        y, v11[0][0], v11[1][0], 'ok')
