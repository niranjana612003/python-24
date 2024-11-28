from graphics.circle import *
from graphics.rectangle import *
from graphics.graphics2.cuboid import *
from graphics.graphics2.sphere import *

import math

print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 2")

num=int(input("Enter the number to find square root"))
print("The square root of ", num, " is ",math.sqrt(num))

r=int(input("Enter the radius of circle"))
print("The area of circle : ",circle_area(r))
print("The perimeter of circle : ",circle_perimeter(r))

l=int(input("Enter the length of rectangle"))
b=int(input("Enter the breadth of rectangle"))
print("The area of rectangle : ",rectangle_area(l,b))
print("The perimeter of rectangle : ",rectangle_perimeter(l,b))

l=int(input("Enter the length of cuboid"))
w=int(input("Enter the width of cuboid"))
h=int(input("Enter the height of cuboid"))
print("The area of rectangle : ",cuboid_area(l,w,h))
print("The perimeter of rectangle : ",cuboid_perimeter(l,w,h))

r=int(input("Enter the radius of sphere"))
print("The area of rectangle : ",sphere_area(r))
print("The perimeter of rectangle : ",sphere_perimeter(r))

