import matplotlib.pyplot as plt
# Class_square
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

# Square parameter
squares = [10,20,30]
for i in range(len(squares)):
    square_1 = square(squares[i])
    square_1.area()
    square_1.display()