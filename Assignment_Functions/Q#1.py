def calcArea(rad,pi=3.1416):
    result=pi*pow(rad,2)
    return result

radius=int(input("Enter Radius of Circle" ))
print(calcArea(radius))