import numpy as np
import scipy.misc as smp


def create_circle(radius = 10, center = 512):
    data = np.zeros((1024, 1024, 3), dtype=np.uint8)
    squared = radius*radius
    for x in range(0, radius):
        for y in range(0, radius):
            if x*x + y*y <= squared:
                data[center + x, center + y] = [254, 0, 0]
                data[center - x, center - y] = [254, 0, 0]
                data[center + x, center - y] = [254, 0, 0]
                data[center - x, center + y] = [254, 0, 0]
    return data


# Create a 1024x1024x3 array of 8 bit unsigned integers
# data = np.zeros((1024, 1024, 3), dtype=np.uint8)

# data[x, y] = [R, G, B]

# The goal of this script is to draw a simple circle.
# The equation to follow is: x^2 + y^2 <= r^2
# CENTER_POINT = 512
# data[CENTER_POINT, CENTER_POINT] = [254, 0, 0]       # Makes the middle pixel red
data = create_circle(100)
img = smp.toimage(data)       # Create a PIL image
img.show()                      # View in default viewer