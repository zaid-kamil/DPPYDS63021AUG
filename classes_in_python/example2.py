
class Chair:
    legs = 4
    def __init__(self, material, color, price=600):
        print('this is the constructor')
        self.material = material
        self.color = color
        self.price = price
        
    def display(self):
        print('display chair detail')
        print('material:', self.material)
        print('color:', self.color)
        print('price:', self.price)
        print('legs', self.legs)
c1 = Chair('Wood', 'red', 700)
c2 = Chair('Wood', 'brown')
c3 = Chair('Plastic', 'blue',300)
c1.display()
c2.display()
c3.display()
c1.material = 'Plastic'
c1.color = 'blue'
c1.price = 1700
c1.display()