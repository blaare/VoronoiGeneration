import random

import numpy as np
import scipy.misc as smp


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

                if x_max and y_max:
                    data[x_plus, y_plus] = [r, g, b]
                if x_min and y_min:
                    data[x_minus, y_minus] = [r, g, b]
                if x_max and y_min:
                    data[x_plus, y_minus] = [r, g, b]
                if x_min and y_max:
                    data[x_minus, y_plus] = [r, g, b]


# Create a 1024x1024x3 array of 8 bit unsigned integers
# data = np.zeros((1024, 1024, 3), dtype=np.uint8)

# data[x, y] = [R, G, B]

# The goal of this script is to draw a simple circle.
# The equation to follow is: x^2 + y^2 <= r^2
# CENTER_POINT = 512
# data[CENTER_POINT, CENTER_POINT] = [254, 0, 0]       # Makes the middle pixel red
datum = np.zeros((1024, 1024, 3), dtype=np.uint8)
print(datum[0,0])
for i in range(0, 10):
    create_circle(datum, 100, random.randint(1, 1024), random.randint(1, 1024), 1024, random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))

img = smp.toimage(datum)       # Create a PIL image
img.show()                      # View in default viewer
