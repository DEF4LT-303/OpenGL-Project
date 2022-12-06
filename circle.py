from OpenGL.GL import *

# PACMAN CIRCLE


def drawCurve(radius, x, y, pos_x, pos_y):
    x1 = x
    y1 = y
    x = 0
    y = radius
    d = 5 - (4 * radius)

    while x < y:

        glColor3f(1.0, 1.0, 0.0)
        glPointSize(1)
        glBegin(GL_POINTS)

        # glVertex2f(pos + x1 + y, pos + y1 + x)      #zone-1
        glVertex2f(pos_x + x1 + x, pos_y + y1 + y)  # zone-2
        glVertex2f(pos_x + x1 - x, pos_y + y1 + y)  # zone-3
        glVertex2f(pos_x + x1 - y, pos_y + y1 + x)  # zone-4
        glVertex2f(pos_x + x1 - y, pos_y + y1 - x)  # zone-5
        glVertex2f(pos_x + x1 - x, pos_y + y1 - y)  # zone-6
        glVertex2f(pos_x + x1 + x, pos_y + y1 - y)  # zone-7
        # glVertex2f(pos + x1 + y, pos + y1 - x)      #zone-8

        glEnd()

        if d < 0:

            # choose east

            d = d + ((16 * x) + 24)  # 8*((2*x)+3)
            x = x + 1

        else:
            # choosing south east

            d = d + ((16 * x) - (16 * y) + 40)  # 8*((2*x)-(2*y)+5)
            x = x + 1
            y = y - 1

    glBegin(GL_LINES)

    glVertex2f(pos_x + x, pos_y + y)
    glVertex2f(pos_x, pos_y)

    glVertex2f(pos_x + x, pos_y + -y)
    glVertex2f(pos_x, pos_y)

    glEnd()
