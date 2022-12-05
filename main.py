from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import numpy as np
import math

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
        glVertex2f(pos_x + x1 + x, pos_y + y1 + y)      #zone-2
        glVertex2f(pos_x + x1 - x, pos_y + y1 + y)      #zone-3
        glVertex2f(pos_x + x1 - y, pos_y + y1 + x)      #zone-4
        glVertex2f(pos_x + x1 - y, pos_y + y1 - x)      #zone-5
        glVertex2f(pos_x + x1 - x, pos_y + y1 - y)      #zone-6
        glVertex2f(pos_x + x1 + x, pos_y + y1 - y)      #zone-7
        # glVertex2f(pos + x1 + y, pos + y1 - x)      #zone-8

        glEnd()



        if d < 0:

            # choose east

            d = d + ((16 * x) + 24) #8*((2*x)+3)
            x = x + 1

        else:
            # choosing south east

            d = d + ((16 * x) - (16 * y) + 40) #8*((2*x)-(2*y)+5)
            x = x + 1
            y = y - 1

    glBegin(GL_LINES)

    glVertex2f(pos_x + x, pos_y + y)
    glVertex2f(pos_x, pos_y)

    glVertex2f(pos_x + x, pos_y + -y)
    glVertex2f(pos_x, pos_y)

    glEnd()

def food(x, y):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5)
    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()

def obstacles():

    x_max = 1500
    y_max = 1000
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
    glVertex2f(x_max, y_max-border)
    glVertex2f(min, y_max-border)

    glVertex2f(x_max, y_max)
    glVertex2f(x_max, min)
    glVertex2f(x_max-border, min)
    glVertex2f(x_max-border, y_max)


    # Obstacles

    glEnd()

    # glColor3f(1, 0, 0)
    # glPointSize(10)
    # glBegin(GL_POINTS)
    # glVertex2f(x_max-border, min)
    # glEnd()

def iterate():
    glViewport(0, 0, 1500, 1500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1500, 0.0, 1500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glLoadIdentity()
    # iterate()


    pygame.init()
    display = (1500, 1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glOrtho(0, 1500, 1000, 0, -1, 1)

    radius = 50
    x = 750
    y = 500

    food_x = 800
    food_y = 500

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT or event.key == ord('a'):
                    x -= 50
                elif event.type == pygame.K_RIGHT or event.key == ord('d'):
                    x += 50
                elif event.type == pygame.K_UP or event.key == ord('w'):
                    y -= 50
                elif event.type == pygame.K_DOWN or event.key == ord('s'):
                    y += 50
        # print(x)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if x > 1500-radius:
            x = 1500-radius

        if x < 0+radius:
            x = 0+radius

        if y > 1000-radius:
            y = 1000-radius

        if y < 0+radius:
            y = 0+radius


        food(food_x, food_y)
        # food(food_x+100, food_y)
        # food(food_x+200, food_y)
        # food(food_x+300, food_y+100)
        # food(food_x+400, food_y)

        # glBegin(GL_POINTS)
        # glVertex2f(food_x, food_y)
        # glEnd()


        drawCurve(radius, 0, 0, x, y)
        obstacles()

        if x == food_x and y == food_y:
            print('test')
            food_x = 2000
            food_y = 2000
            food(food_x, food_y)

        pygame.display.flip()
        pygame.time.wait(10)
    # glutSwapBuffers()

showScreen()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(1500, 1500)  # window size
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
# glutDisplayFunc(showScreen)
#
# glutMainLoop()