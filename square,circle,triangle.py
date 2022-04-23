import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math
import numpy as np

# Class Square
class  square:

    def __init__(self,side):
        self.side = side

    def area(self):
        print("Area = " + str(self.side) + " m^2")

    def display(self):
        square = plt.Rectangle((0,0),self.side, self.side, fc='blue',ec="red")
        plt.gca().add_patch(square)
        plt.axis('scaled')
        plt.show()

# Class Circle
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius**2
        print("Area = " + str(area) + " m^2")

    def display(self):
        plt.axes()
        circle = plt.Circle((0,0),self.radius, fc='blue',ec="red")
        plt.gca().add_patch(circle)
        plt.axis('scaled')
        plt.show()

# Class Triangle
class triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        area = (self.base * self.height)/2
        print("Area = " + str(area) + " m^2")

    def display(self):
        pts = np.array([[3,self.base], [self.height,1], [1,1]])
        p = Polygon(pts, closed=False)
        ax = plt.gca()
        ax.add_patch(p)
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)
        plt.show()

# List of squares
squares = [10,20,30]
for i in range(len(squares)):
    square_1 = square(squares[i])
    square_1.area()
    square_1.display()

# Lists of circles
circles = [10,20,30]
for i in range(len(circles)):
    circle_1 = circle(circles[i])
    circle_1.area()
    circle_1.display()

# List of triangles
triangles = [[2,2],[3,3],[4,4]]
for i in range(len(triangles)):
    b = triangles[i][0]
    h = triangles[i][1]
    triangle_1 = triangle(b,h)
    triangle_1.area()
    triangle_1.display()