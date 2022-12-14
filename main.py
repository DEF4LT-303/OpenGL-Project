### Please install pygame (pip install pygame) before runnung ###

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import numpy as np
import math
import random
import time

from circle import *
from lines import *
from food import *
from boundary import *
from map import *
from checkobstacle import *
from enemy import *


def showScreen():

    food_cords = []
    radius = 25
    x = 10
    y = 75

    print(food_cords)

    score = 0

    ult_food_x = 375                              # Generate ultimate food item
    ult_food_y = 250

    for i in range(10):														# Generate food items

        food_x = random.randint(51, 680)
        food_x -= food_x % 25
        food_y = random.randint(51, 400)
        food_y -= food_y % 25

        flag = food_check(food_x, food_y, radius)

        while flag:                               # Check if food is not generated on the obstacle

            food_x = random.randint(50, 680)
            food_x -= food_x % 25
            food_y = random.randint(50, 400)
            food_y -= food_y % 25
            flag = food_check(food_x, food_y, radius)

        food_cords.append([food_x, food_y])

    pygame.init()                 # Initialize pygame

    display = (750, 500)
    # Set display wtih OpenGL
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # glOrtho(0, 750, 500, 0, -1, 1)
    glOrtho(0, 750, 0, 500, -1, 1)

    font = pygame.font.Font('freesansbold.ttf', 23)

    def drawText(x, y, text):
        textSurface = font.render(
            text, True, (0, 255, 0, 0), (0, 0, 0, 0))
        # textSurface = font.render(text, True, (255, 255, 255, 255), (255, 255, 255, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData)

    def drawTextWin(x, y, text):
        textSurface = font.render(
            text, True, (0, 255, 0, 0), (0, 0, 0, 0))
        #textSurface = font.render(text, True, (255, 255, 255, 255), (255, 255, 255, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData)

    def drawTextEnd():
        textSurface = font.render(
            "Winner!", True, (0, 255, 0, 0), (0, 0, 0, 0))
        #textSurface = font.render(text, True, (255, 255, 255, 255), (255, 255, 255, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(20, 410)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData)

    def drawMapText():  # start and goal text
        textSurface1 = font.render(
            'START', True, (255, 255, 255, 255), (0, 0, 0, 0))
        textData1 = pygame.image.tostring(textSurface1, "RGBA", True)
        glWindowPos2d(10, 20)
        glDrawPixels(textSurface1.get_width(), textSurface1.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData1)

        textSurface2 = font.render(
            'EXIT', True, (255, 255, 255, 255), (0, 0, 0, 0))
        textData2 = pygame.image.tostring(textSurface2, "RGBA", True)
        glWindowPos2d(680, 370)
        glDrawPixels(textSurface2.get_width(), textSurface2.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData2)

    status = True
    pause = False
    tx = 0
    ty = 0
    flag = 0
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
                    y += 25
                elif event.key == pygame.K_DOWN:  # or event.key == ord('s'):
                    y -= 25

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if x > 750 - radius:            # Boundaries of the character movement
            x = 750 - radius

        if x < 0 + radius+10:
            x = 0 + radius+25

        if y > 500 - radius-10:
            y = 500 - radius-25

        if y < 0 + radius+10:
            y = 0 + radius+25

        boundary()                         # Draw the  boundaries
        # enemy()
        enemy_translate(tx, ty)

        i, j = enemy_path()
        tx += i
        ty += j

        x, y = enemy_check(x, y, radius)
        drawCurve(radius, x, y)       # Draw the character

        for i in range(len(food_cords)):		# Draw the food items
            food(food_cords[i][0], food_cords[i][1])

        ultimate_food(ult_food_x, ult_food_y)

        for i in range(len(food_cords)):		# Check if the character has eaten the food
            if x == food_cords[i][0] and y == food_cords[i][1]:
                food_cords[i][0] = 2000
                food_cords[i][1] = 2000

                score += 1

            if x == ult_food_x and y == ult_food_y:		# Check if the character has eaten the ultimate food
                ult_food_x = 2000
                ult_food_y = 2000
                score += 10

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

        drawlines_map()             # Draw the map
        x, y = check(x, y, radius)  # checking the obstacles

        drawText(20, 450, "Score:")

        if score == len(food_cords)+10:  # Check if the game is over
            drawTextWin(310, 410, "Go to Exit!")
            # pause = True

        drawMapText()

        if x >= 700 and x <= 725 and y == 375:
            drawTextEnd()

        pygame.display.flip()  # Update the full display Surface to the screen
        pygame.time.wait(10)  # pause the program for an amount of time


showScreen()
