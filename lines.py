from OpenGL.GL import *
import numpy as np


def draw_points(x, y):

    # first we scale the points
    sc = 0.2
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])

    # then we translate the points
    tx = 500
    ty = 2000
    trasnlate = np.array([[1, 0, tx],
                          [0, 1, ty],
                          [0, 0, 1]])

    st = np.matmul(s, trasnlate)  # scale and translate

    v1 = np.array([[x],
                  [y],
                  [1]])

    v11 = np.matmul(st, v1)  # scale and translate points

    glPointSize(3)
    glBegin(GL_POINTS)
    # glVertex2f(x, y)
    glVertex2f(v11[0][0], v11[1][0])  # print scaled points
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
