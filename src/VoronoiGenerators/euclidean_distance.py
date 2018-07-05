import pathlib
import random

import imageio as imageio
import numpy
import scipy
import string

import numpy as np
from scipy.misc import imsave
import scipy.misc as smp


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def check_if_zero(a):
    for item in a:
        if item != 0:
            return False
    return True


def create_circle(data, radius=10, center_x=512, center_y=512, resolution=1024, r=254, g=0, b=0):
    squared = radius*radius
    for x in range(0, radius):
        for y in range(0, radius):
            if x*x + y*y <= squared:
                x_minus = center_x - x
                x_plus = center_x + x
                y_minus = center_y - y
                y_plus = center_y + y

                x_min = x_minus > 0
                x_max = x_plus < resolution
                y_min = y_minus > 0
                y_max = y_plus < resolution

                if x_max and y_max and check_if_zero(data[x_plus, y_plus]):
                    data[x_plus, y_plus] = [r, g, b]
                if x_min and y_min and check_if_zero(data[x_minus, y_minus]):
                    data[x_minus, y_minus] = [r, g, b]
                if x_max and y_min and check_if_zero(data[x_plus, y_minus]):
                    data[x_plus, y_minus] = [r, g, b]
                if x_min and y_max and check_if_zero(data[x_minus, y_plus]):
                    data[x_minus, y_plus] = [r, g, b]


# Create a 1024x1024x3 array of 8 bit unsigned integers
# data = np.zeros((1024, 1024, 3), dtype=np.uint8)

# data[x, y] = [R, G, B]

# The goal of this script is to draw a simple circle.
# The equation to follow is: x^2 + y^2 <= r^2
# CENTER_POINT = 512
# data[CENTER_POINT, CENTER_POINT] = [254, 0, 0]       # Makes the middle pixel red
datum = np.zeros((1024, 1024, 3), dtype=np.uint8)
print(datum[0, 0])
vertices = []
for i in range(0, 50):
    vertices.append([random.randint(1, 1024), random.randint(1, 1024),
                     random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)])

# size
for i in range(0, 300):
    print("%d \r" % i)
    # iterations/ number of circles
    for j in range(1, 10):
        create_circle(datum, i, vertices[j][0], vertices[j][1], 1024, vertices[j][2], vertices[j][3], vertices[j][4])
    # Create a PIL image
imageio.imwrite('../../sample_images/'+id_generator()+".png", numpy.asarray(datum))       # Create a PIL image

