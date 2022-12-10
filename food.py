from OpenGL.GL import *


def food(x, y):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5)
    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()


def ultimate_food(x, y):
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(10)
    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()
