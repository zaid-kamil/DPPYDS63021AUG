class Shape:
    def __init__(self, h, w):
        self.h = h
        self.w = w
    
    def area(self):
        return self.h * self.w

class Triangle(Shape): 
  
    # Override area method
    def area(self):
        return 1/2 * self.h * self.w

class Square(Shape): 

    def perimeter(self):
        return self.h * 2 + self.w * 2

class Circle(Shape):

    # contructor override
    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * self.h * self.w

# s1 = Shape(5, 10)
# print(s1.area())

# s2 = Triangle(5, 10)
# print(s2.area())

# s3 = Square(5, 10)
# print(s3.area())
# print(s3.perimeter())

# s4 = Circle(5)
# print(s4.area())
