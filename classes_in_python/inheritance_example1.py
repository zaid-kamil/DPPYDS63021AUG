import math
class Calc:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def div(self, x, y):
        return x / y

class ScientificCalc(Calc):
    
    def power(self, x, y):
        return x ** y
    def sqrt(self, x):
        return math.sqrt(x)

c = Calc()
d = ScientificCalc()
print(d.add(1,2))
print(d.sub(1,2))
print(d.power(2,3))