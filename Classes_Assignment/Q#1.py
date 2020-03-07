import math
class Circle:
    def __init__(self):
        self.rad=radius
    def area(self,rad):
        rad=math.pi*pow(rad,2)
        return rad
    def perimeter(self,rad):
        perim=2*math.pi*rad
        return perim
radius=int(input("Enter radius of Circle "))
circle1=Circle()
area=circle1.area(radius)
print("Area of a Circle is ",area)
perimeter=circle1.perimeter(radius)
print("Circumference(Perimeter) of a Circle is ",perimeter)
