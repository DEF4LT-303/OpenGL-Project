from OpenGL.GL import *
import numpy as np
import time

enemy_cords = [[0, 0], [0, 0], [0, 0], [0, 0]]


def enemy(v1, v2, v3, v4):

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)

    # glVertex2f(280, 330)
    # glVertex2f(280, 380)
    # glVertex2f(330, 380)
    # glVertex2f(330, 330)
    glVertex2f(v1[0], v1[1])
    enemy_cords[0] = v1[0], v1[1]
    glVertex2f(v2[0], v2[1])
    enemy_cords[1] = v2[0], v2[1]
    glVertex2f(v3[0], v3[1])
    enemy_cords[2] = v3[0], v3[1]
    glVertex2f(v4[0], v4[1])
    enemy_cords[3] = v4[0], v4[1]

    glEnd()


def enemy_translate(x, y):
    # time.sleep(1)

    translate = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])

    # v1 = np.array([280, 330, 1])
    # v2 = np.array([280, 380, 1])
    # v3 = np.array([330, 380, 1])
    # v4 = np.array([330, 330, 1])
    v1 = np.array([275, 325, 1])
    v2 = np.array([275, 375, 1])
    v3 = np.array([325, 375, 1])
    v4 = np.array([325, 325, 1])

    v1 = np.matmul(translate, v1)
    v2 = np.matmul(translate, v2)
    v3 = np.matmul(translate, v3)
    v4 = np.matmul(translate, v4)

    enemy(v1, v2, v3, v4)
    # print(enemy_cords[0][0], enemy_cords[0][1])


def enemy_path():

    x = 0
    y = 0
    if enemy_cords[0][0] == 450 and enemy_cords[0][1] >= 160:
        x = 0
        y = -25

    elif enemy_cords[0][0] < 450 and enemy_cords[0][1] == 325:
        x = 25
        y = 0

    elif enemy_cords[0][0] == 275 and enemy_cords[0][1] <= 325:
        x = 0
        y = 25

    elif enemy_cords[0][0] >= 275 and enemy_cords[0][1] <= 160:
        x = -25
        y = 0

    # print(x, y)

    return x, y


def enemy_check(x, y, radius):

    if y == enemy_cords[0][1] and (x >= enemy_cords[0][0] and x <= enemy_cords[3][0]):  # down
        x = 300
        y = 100

    # left
    elif x == enemy_cords[1][0] and (y >= enemy_cords[0][1] and y <= enemy_cords[1][1]):
        x = 300
        y = 100

    elif y == enemy_cords[1][1] and (x >= enemy_cords[1][0] and x <= enemy_cords[2][0]):  # up
        x = 300
        y = 100

    # right
    elif x == enemy_cords[2][0] and (y >= enemy_cords[2][1] and y <= enemy_cords[3][1]):
        x = 300
        y = 100

    return x, y
