# import inheritance_override 
# import inheritance_override as iho
from inheritance_override import Circle, Square
# from inheritance_override import * 

# according to normal import
# cir = inheritance_override.Circle(4)
# rec = inheritance_override.Square(4, 4)
# tri = inheritance_override.Triangle(4, 4)

# according to import alias
# cir = iho.Circle(4)
# rec = iho.Square(4, 4)
# tri = iho.Triangle(4, 4)

# importing specific classes from a module
cir = Circle(4)
rec = Square(4, 4)

# importing all classes from a module using *
# cir = Circle(4)
# rec = Square(4, 4)
# tri = Triangle(4, 4)

print(cir.area())
print(rec.area())
# print(tri.area())
