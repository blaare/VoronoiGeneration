import imageio
import numpy
import numpy as np
import os
import sys
import random


class Voronoi:

    def __init__(self):
        self.x = 1024
        self.y = 1024
        self.z = 3
        self.datum = np.zeros((self.x, self.y, self.z), dtype=np.uint8)
        self.resolution = self.x
        self.vertex_count = 10
        self.vertices = []
        self.circle_count = self.vertex_count
        self.circle_size = 450

    @staticmethod
    def check_if_zero(a):
        for item in a:
            if item != 0:
                return False
        return True

    def create_circle(self, radius, center_x, center_y, r, g, b):
        squared = radius * radius
        for x in range(0, radius):
            for y in range(0, radius):
                if squared >= x*x + y*y:
                    x_neg = center_x - x
                    x_plu = center_x + x
                    y_neg = center_y - y
                    y_plu = center_y + y

                    x_min = x_neg > 0
                    x_max = x_plu < self.resolution
                    y_min = y_neg > 0
                    y_max = y_plu < self.resolution

                    if x_max and y_max and self.check_if_zero(self.datum[x_plu, y_plu]):
                        self.datum[x_plu, y_plu] = [r, g, b]
                    if x_min and y_min and self.check_if_zero(self.datum[x_neg, y_neg]):
                        self.datum[x_neg, y_neg] = [r, g, b]
                    if x_max and y_min and self.check_if_zero(self.datum[x_plu, y_neg]):
                        self.datum[x_plu, y_neg] = [r, g, b]
                    if x_min and y_max and self.check_if_zero(self.datum[x_neg, y_plu]):
                        self.datum[x_neg, y_plu] = [r, g, b]

    @staticmethod
    def clear_turn_into_gif():
        folder = '../../../sample_images/turn_into_gif/'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    def generate_vertices(self):
        for i in range(0, self.vertex_count):
            self.vertices.append(
                [random.randint(1, self.x), random.randint(1, self.y), random.randint(1, 254), random.randint(1, 254),
                 random.randint(1, 254)])

    def fill_circles(self):
        color = 0
        for i in range(0, self.circle_size):
            print("%d \r" % i)
            for j in range(0, 10):
                print("%d \r" % j)
                self.create_circle(i, self.vertices[j][0], self.vertices[j][1], color,
                                   color, color)
                color+=1
            imageio.imwrite('../../../sample_images/turn_into_gif/' + str(i) + ".png",
                            numpy.asarray(self.datum))

    def run(self):
        self.clear_turn_into_gif()
        self.generate_vertices()
        self.fill_circles()


a = Voronoi()
a.run()

