from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import numpy as np
import math
import random

from circle import *
from lines import *
from food import *
from obstacles import *


# def iterate():
#     glViewport(0, 0, 750, 750)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 750, 0.0, 750, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


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

    pygame.init()                 # Initialize pygame
    display = (750, 500)
    # Set display wtih OpenGL
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, 750, 500, 0, -1, 1)

    radius = 25
    x = 375
    y = 350

    food_x1 = 400
    food_y1 = 250
    score = 0

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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if x > 750 - radius:            # Boundaries of the character movement
            x = 750 - radius

        if x < 0 + radius:
            x = 0 + radius

        if y > 500 - radius:
            y = 500 - radius

        if y < 0 + radius:
            y = 0 + radius

        obstacles()

        food(food_x1, food_y1)
        food(food_x2, food_y2)
        food(food_x3, food_y3)
        food(food_x4, food_y4)
        food(food_x5, food_y5)

        drawCurve(radius, 0, 0, x, y)       # Draw the character

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

        if score < 10:                # Display the score
            id = "0" + str(score)

        else:
            id = str(score)

        second = int(id[-1])
        first = int(id[-2])

        g = 0
        drawlines(first, g)
        g = 150
        drawlines(second, g)

        pygame.display.flip()  # Update the full display Surface to the screen
        pygame.time.wait(10)  # pause the program for an amount of time


showScreen()
