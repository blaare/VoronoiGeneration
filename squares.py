import random
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
        for y in range(0, radius-5):
            if squared >= x + y:
                x_neg = center_x - x
                x_plu = center_x + x
                y_neg = center_y - y
                y_plu = center_y + y

                x_min = x_neg > 0
                x_max = x_plu < resolution
                y_min = y_neg > 0
                y_max = y_plu < resolution

                if x_max and y_max and check_if_zero(data[x_plu, y_plu]):
                    data[x_plu, y_plu] = [r, g, b]
                if x_min and y_min and check_if_zero(data[x_neg, y_neg]):
                    data[x_neg, y_neg] = [r, g, b]
                if x_max and y_min and check_if_zero(data[x_plu, y_neg]):
                    data[x_plu, y_neg] = [r, g, b]
                if x_min and y_max and check_if_zero(data[x_neg, y_plu]):
                    data[x_neg, y_plu] = [r, g, b]


datum = np.zeros((1024, 1024, 3), dtype=np.uint8)
print(datum[0, 0])
vertices = []
for i in range(0, 100):
    # x | y | color
    vertices.append([random.randint(1, 1024), random.randint(1, 1024), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)])
# size
for i in range(0, 125):
    print("%d \r" % i)
    # iterations/ number of circles
    for j in range(0, 100):
        create_circle(datum, i, vertices[j][0], vertices[j][1], 1024, vertices[j][2], vertices[j][3], vertices[j][4])
imsave("./sample_images/"+id_generator()+".png", smp.toimage(datum))       # Create a PIL image
