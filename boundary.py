from OpenGL.GL import *


def boundary():
    x_max = 750
    y_max = 500
    min = 0
    border = 10
    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)

    # Boundaries
    glVertex2f(min, min)
    glVertex2f(x_max, min)
    glVertex2f(x_max, border)
    glVertex2f(min, border)

    glVertex2f(min, min)
    glVertex2f(min, y_max)
    glVertex2f(border, y_max)
    glVertex2f(border, min)

    glVertex2f(min, y_max)
    glVertex2f(x_max, y_max)
    glVertex2f(x_max, y_max - border)
    glVertex2f(min, y_max - border)

    glVertex2f(x_max, y_max)
    glVertex2f(x_max, min)
    glVertex2f(x_max - border, min)
    glVertex2f(x_max - border, y_max)

    # Obstacles

    glEnd()

    # glColor3f(1, 0, 0)
    # glPointSize(10)
    # glBegin(GL_POINTS)
    # glVertex2f(x_max-border, min)
    # glEnd()
