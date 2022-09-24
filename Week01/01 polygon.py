class Polygon:
    def __init__(self, sides_numbers):
        self.n = sides_numbers
        self.sides = [0 for i in range(sides_numbers)]

    def read_sides(self):
        self.sides = [float(input("Enter side size "+ str(i+1) + ": " ) )
        for i in range(self.n)]

    def show_sides(self):
        for i in range(self.n):
            print("Side", i+1, "size is", self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def area(self):
        a, b, c = self.sides
        # perimeter calc
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The triangle area is %0.2f" %area)


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def show_sides(self):
        side1 = float(input("Enter a side 1 :"))
        side2 = float(input("Enter a side 2 :"))
        self.sides[0] = self.sides[2] = side1
        self.sides[1] = self.sides[3] = side2

    def area(self):
        return self.sides[0] * self.sides[1]

    def diagonal(self):
        return (self.sides[0]**2 + self.sides[1]**2)** 0.5

class RightTriangle(Triangle):
    def isRightTriangle(self):
        return(self.sides[0]**2 == self.sides[1]**2 + self.sides[2]**2 or self.sides[1]**2 == self.sides[2]**2 + self.sides[0]**2 or self.sides[2]**2 == self.sides[0]**2 + self.sides[1]**2)