def calcArea(rad,pi=3.1416):
    result=pi*pow(rad,2)
    return result
again=input("Do you want to Continue:[Y/N] ")
while again=='Y':
    radius = int(input("Enter Radius of Circle "))
    print(calcArea(radius))
    again = input("Do you want to Continue:[Y/N] ")
