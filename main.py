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
from boundary import *
from map import *
from checkobstacle import *


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

    food_cords = []

    for i in range(7):														# Generate food items
        food_x = random.randint(15, 680)
        food_x -= food_x % 25
        food_y = random.randint(15, 430)
        food_y -= food_y % 25
        food_cords.append([food_x, food_y])

    pygame.init()                 # Initialize pygame

    display = (750, 500)
    # Set display wtih OpenGL
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, 750, 500, 0, -1, 1)

    radius = 25
    x = 10
    y = 0

    score = 0

    font = pygame.font.Font('freesansbold.ttf', 23)

    def drawText(x, y, text):
        textSurface = font.render(
            'Score:', True, (0, 255, 0, 0), (0, 0, 0, 0))
        #textSurface = font.render(text, True, (255, 255, 255, 255), (255, 255, 255, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData)

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

        if x < 0 + radius+10:
            x = 0 + radius+25

        if y > 500 - radius-10:
            y = 500 - radius-25

        if y < 0 + radius+10:
            y = 0 + radius+25

        obstacles()

        drawCurve(radius, 0, 0, x, y)       # Draw the character

        for i in range(len(food_cords)):		# Draw the food items
            food(food_cords[i][0], food_cords[i][1])

        for i in range(len(food_cords)):		# Check if the character has eaten the food
            if x == food_cords[i][0] and y == food_cords[i][1]:
                food_cords[i][0] = 2000
                food_cords[i][1] = 2000

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

        drawlines_map()
        x, y = check(x, y, radius)  # checking the obstacles

        drawText(20, 50, "Score")
        pygame.display.flip()  # Update the full display Surface to the screen
        pygame.time.wait(10)  # pause the program for an amount of time


showScreen()
