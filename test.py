from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import numpy as np
import math
import random


def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        elif dx > 0 and dy < 0:
            return 7

    elif abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        elif dx > 0 and dy < 0:
            return 6


def ConvertToZone0(x1, y1, x2, y2, zone):
    if zone == 0:
        return x1, y1, x2, y2
    elif zone == 1:
        return y1, x1, y2, x2
    elif zone == 2:
        return y1, -x1, y2, -x2
    elif zone == 3:
        return -x1, y1, -x2, y2
    elif zone == 4:
        return -x1, -y1, -x2, -y2
    elif zone == 5:
        return -y1, -x1, -y2, -x1
    elif zone == 6:
        return -y1, x1, -y2, x2
    elif zone == 7:
        return x1, -y1, x2, -y2


def OriginalZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def mid_point_line(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1, x2, y2 = ConvertToZone0(x1, y1, x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    NE = (2 * dy) - (2 * dx)
    E = 2 * dy

    x = x1
    y = y1

    while (x <= x2):

        original_x, original_y = OriginalZone(x, y, zone)
        draw_points(original_x, original_y)

        if d > 0:
            d = d + NE
            x = x + 1
            y = y + 1
        else:
            d = d + E
            x = x + 1


def drawlines(num, x):
    glColor3f(0, 1, 0)

    if num == 0:
        mid_point_line(100 + x, 350, 210 + x, 350)
        mid_point_line(100 + x, 150, 100 + x, 350)
        mid_point_line(210 + x, 150, 210 + x, 350)
        mid_point_line(100 + x, 150, 210 + x, 150)

    elif num == 1:
        mid_point_line(210 + x, 150, 210 + x, 350)

    elif num == 2:
        mid_point_line(100 + x, 350, 200 + x, 350)
        mid_point_line(100 + x, 250, 100 + x, 350)
        mid_point_line(100 + x, 250, 200 + x, 250)
        mid_point_line(200 + x, 150, 200 + x, 250)
        mid_point_line(100 + x, 150, 200 + x, 150)

    elif num == 3:
        mid_point_line(100 + x, 350, 200 + x, 350)
        mid_point_line(200 + x, 250, 200 + x, 350)
        mid_point_line(100 + x, 250, 200 + x, 250)
        mid_point_line(200 + x, 150, 200 + x, 250)
        mid_point_line(100 + x, 150, 200 + x, 150)

    elif num == 4:
        mid_point_line(100 + x, 150, 100 + x, 250)
        mid_point_line(100 + x, 250, 200 + x, 250)
        mid_point_line(200 + x, 250, 200 + x, 350)
        mid_point_line(200 + x, 150, 200 + x, 250)

    elif num == 5:
        mid_point_line(100 + x, 350, 200 + x, 350)
        mid_point_line(200 + x, 250, 200 + x, 350)
        mid_point_line(100 + x, 250, 200 + x, 250)
        mid_point_line(100 + x, 150, 100 + x, 250)
        mid_point_line(100 + x, 150, 200 + x, 150)


    elif num == 6:
        mid_point_line(100 + x, 350, 200 + x, 350)
        mid_point_line(100 + x, 250, 100 + x, 350)
        mid_point_line(100 + x, 250, 200 + x, 250)
        mid_point_line(100 + x, 150, 100 + x, 250)
        mid_point_line(200 + x, 250, 200 + x, 350)
        mid_point_line(100 + x, 150, 200 + x, 150)

    elif num == 7:
        mid_point_line(100 + x, 150, 210 + x, 150)
        mid_point_line(210 + x, 150, 210 + x, 350)

    elif num == 8:
        mid_point_line(100 + x, 350, 210 + x, 350)
        mid_point_line(100 + x, 150, 100 + x, 350)
        mid_point_line(100 + x, 250, 210 + x, 250)
        mid_point_line(210 + x, 150, 210 + x, 350)
        mid_point_line(100 + x, 150, 210 + x, 150)

    else:
        mid_point_line(100 + x, 350, 200 + x, 350)
        mid_point_line(200 + x, 250, 200 + x, 350)
        mid_point_line(100 + x, 250, 200 + x, 250)
        mid_point_line(200 + x, 150, 200 + x, 250)
        mid_point_line(100 + x, 150, 100 + x, 250)
        mid_point_line(100 + x, 150, 200 + x, 150)

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


def food(x, y):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5)
    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()


def obstacles():
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


def iterate():
    glViewport(0, 0, 750, 750)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 750, 0.0, 750, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glLoadIdentity()
    # iterate()

    food_x2 = random.randint(0, 700)
    food_x2 -= food_x2 % 25
    food_y2 = random.randint(0, 450)
    food_y2 -= food_y2 % 25

    food_x3 = random.randint(0, 700)
    food_x3 -= food_x3 % 25
    food_y3 = random.randint(0, 450)
    food_y3 -= food_y3 % 25

    food_x4 = random.randint(0, 700)
    food_x4 -= food_x4 % 25
    food_y4 = random.randint(0, 450)
    food_y4 -= food_y4 % 25

    food_x5 = random.randint(0, 700)
    food_x5 -= food_x5 % 25
    food_y5 = random.randint(0, 450)
    food_y5 -= food_y5 % 25

    pygame.init()
    display = (750, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, 750, 500, 0, -1, 1)
    radius = 25
    x = 375
    y = 350

    food_x1 = 400
    food_y1 = 250
    score = 14

    # foodArr = []
    # for i in range(6):
    #     xf = random.randint(0,700)
    #     yf = random.randint(0,450)
    #     foodArr.append(xf)
    #     foodArr.append(yf)
    # print(foodArr)

    status = True
    while status:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # or event.key == ord('a'):
                    x -= 25
                elif event.key == pygame.K_RIGHT:  # or event.key == ord('d'):
                    x += 25
                elif event.key == pygame.K_UP:  # or event.key == ord('w'):
                    y -= 25
                elif event.key == pygame.K_DOWN:  # or event.key == ord('s'):
                    y += 25
        # print(x)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if x > 750 - radius:
            x = 750 - radius

        if x < 0 + radius:
            x = 0 + radius

        if y > 500 - radius:
            y = 500 - radius

        if y < 0 + radius:
            y = 0 + radius

        obstacles()
        # for j in range(0,len(foodArr),2):
        #     food(foodArr[j], foodArr[j+1])

        food(food_x1, food_y1)
        food(food_x2, food_y2)
        food(food_x3, food_y3)
        food(food_x4, food_y4)
        food(food_x5, food_y5)

        drawCurve(radius, 0, 0, x, y)

        if x == food_x1 and y == food_y1:
            print('hh')
            food_x1 = 2000
            food_y1 = 2000
            food(food_x1, food_y1)
            score += 1
        elif x == food_x2 and y == food_y2:
            print('hh1')
            # food_x2 = 2000
            # food_y2 = 2000
            food_x2 = random.randint(0, 700)
            food_x2 -= food_x2 % 25
            food_y2 = random.randint(0, 450)
            food_y2 -= food_y2 % 25
            food(food_x2, food_y2)
            score += 1
        elif x == food_x3 and y == food_y3:
            print('hh2')
            food_x3 = 2000
            food_y3 = 2000
            food(food_x3, food_y3)
            score += 1
        elif x == food_x4 and y == food_y4:
            print('hh3')
            food_x4 = 2000
            food_y4 = 2000
            food(food_x4, food_y4)
            score += 1
        elif x == food_x5 and y == food_y5:
            print('hh4')
            food_x5 = 2000
            food_y5 = 2000
            food(food_x5, food_y5)
            score += 1

        if score < 10:
            id = "0" + str(score)

        else:
            id = str(score)

        second = int(id[-1])
        first = int(id[-2])

        g = 0
        drawlines(first, g)
        g = 150
        drawlines(second, g)

        print(score)

        pygame.display.flip()  # Update the full display Surface to the screen
        pygame.time.wait(10)  # pause the program for an amount of time
    # glutSwapBuffers()


showScreen()