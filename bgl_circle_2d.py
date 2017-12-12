import bpy
import bgl
from math import pi, cos, sin

def circle_2d(x, y, rad, start, end, step):

    ang = start
    while(ang < end):
        bgl.glVertex2f(x+rad*cos(ang), y+rad*sin(ang))

        ang += 2*pi / step