from OpenGL.GL import *
import numpy as np


def draw_points(x, y, stat):

    if stat != None:
        glPointSize(1)
        glColor3f(1.0, 1.0, 0.0)
    else:
        glPointSize(4)
        glColor3f(.0, .0, .5)
    glBegin(GL_POINTS)
    glVertex2f(.8, .8)
    glVertex2f(x, y)
    glEnd()


def whichZone(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4


def convert_to_zone0(region, x, y):
    if region == 0:
        return x, y
    if region == 1:
        return y, x
    if region == 2:
        return y, -x
    if region == 3:
        return -x, y
    if region == 4:
        return -x, -y
    if region == 5:
        return -y, -x
    if region == 6:
        return -y, x
    if region == 7:
        return x, -y


def convert_original(region, x, y):

    if region == 0:
        return x, y
    if region == 1:
        return y, x
    if region == 2:
        return -y, x
    if region == 3:
        return -x, y
    if region == 4:
        return -x, -y
    if region == 5:
        return -y, -x
    if region == 6:
        return y, -x
    if region == 7:
        return x, -y


def midpointline(x1, y1, x2, y2, z, status):
    # print("midpointLine", (x1,y1),(x2,y2))
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_points(px, py, status)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne


def draw_midpoint_lines(x1, y1, x2, y2, flag=None):
    dx = x2 - x1
    dy = y2 - y1

    zone = whichZone(dx, dy)

    pxl1, pyl1 = convert_to_zone0(zone, x1, y1)
    pxl2, pyl2 = convert_to_zone0(zone, x2, y2)

    midpointline(pxl1, pyl1, pxl2, pyl2, zone, flag)


def drawlines_map():
    draw_midpoint_lines(150, 0, 150, 250)  # firstvertical
    draw_midpoint_lines(275, 150, 375, 150)  # secondhorizontal
    draw_midpoint_lines(275, 180, 275, 390)  # thirdvertical
    draw_midpoint_lines(500, 152, 500, 285)  # fourthvertical
    draw_midpoint_lines(625, 285, 625, 390)  # fifthvertical

    draw_midpoint_lines(0, 400, 750, 400)
