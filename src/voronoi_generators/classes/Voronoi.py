import imageio
import numpy
import numpy as np
import os
import sys
import random


class Voronoi:

    def __init__(self, resolution_x=1024, resolution_y=1024, circle_count=10, circle_size=500):
        self.x = resolution_x
        self.y = resolution_y
        self.z = 3
        self.datum = np.zeros((self.x, self.y, self.z), dtype=np.uint8)
        self.vertex_count = circle_count
        self.vertices = []
        self.circle_count = self.vertex_count
        self.circle_size = circle_size

    @staticmethod
    def check_if_zero(a):
        for item in a:
            if item != 0:
                return False
        return True

    def create_circle(self, radius, center_x, center_y, r, g, b):
        squared = radius * radius
        not_created_count = 0
        for x in range(0, radius):
            for y in range(0, radius):
                created = False
                if squared >= x*x + y*y:
                    x_neg = center_x - x
                    x_plu = center_x + x
                    y_neg = center_y - y
                    y_plu = center_y + y

                    x_min = x_neg > 0
                    x_max = x_plu < self.x
                    y_min = y_neg > 0
                    y_max = y_plu < self.y

                    if x_max and y_max and self.check_if_zero(self.datum[x_plu, y_plu]):
                        self.datum[x_plu, y_plu] = [r, g, b]
                        created = True
                    if x_min and y_min and self.check_if_zero(self.datum[x_neg, y_neg]):
                        self.datum[x_neg, y_neg] = [r, g, b]
                        created = True
                    if x_max and y_min and self.check_if_zero(self.datum[x_plu, y_neg]):
                        self.datum[x_plu, y_neg] = [r, g, b]
                        created = True
                    if x_min and y_max and self.check_if_zero(self.datum[x_neg, y_plu]):
                        self.datum[x_neg, y_plu] = [r, g, b]
                        created = True
                if not created:
                    not_created_count += 1
        return not_created_count != squared

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
                [random.randint(int(.1*self.x), self.x), random.randint(int(.1*self.y), self.y),
                 random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)])

    def fill_circles(self):
        factor = int(max(self.x, self.y) / 255) - 1
        color = 0
        skip_circles = dict()
        for k in range(0, self.circle_count):
            skip_circles[k] = False
        for i in range(1, self.circle_size):
            for j in range(1, self.circle_count):
                sys.stdout.write('Radius Size: ' + str(i) + '/' + str(self.circle_size) + ' | ' +
                                 'Current Circle: ' + str(j) + '/' + str(self.circle_count) + ' | ' +
                                 'Color Level: ' + str(color) + '    \r')
                if not skip_circles[j]:
                    circle_created = self.create_circle(i, self.vertices[j][0], self.vertices[j][1], color, color,
                                                        color)
                    if not circle_created:
                        skip_circles[j] = True
                        print("Circle " + str(j) + " Complete")

            if False in skip_circles:
                color += 1 if i % factor == 0 else 0
        imageio.imwrite('../../../sample_images/turn_into_gif/' + str(i) + ".png",
                        numpy.asarray(self.datum))

    def run(self):
        self.clear_turn_into_gif()
        self.generate_vertices()
        self.fill_circles()


a = Voronoi(int(input("Resolution X:")), int(input("Resolution Y:")), int(input("Circle Count:")),
            int(input("Circle Size:")))
a.clear_turn_into_gif()
a.generate_vertices()
a.fill_circles()

