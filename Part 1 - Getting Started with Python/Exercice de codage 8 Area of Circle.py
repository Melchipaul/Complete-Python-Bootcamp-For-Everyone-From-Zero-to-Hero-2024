import math
def circle_area(radius):
    area = math.pi * radius**2
    return area
try:
    radius = float(input("Enter Radius: "))
    print("The area of the circle is: ",circle_area(radius))
except ValueError as err:
    print("Error: ", err)