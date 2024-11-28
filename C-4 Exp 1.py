print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 1")

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):

        return self.length * self.breadth

    def perimeter(self):

        return 2 * (self.length + self.breadth)



a1 = int(input("Enter length of the first rectangle: "))
b1 = int(input("Enter breadth of the first rectangle: "))
rect1 = Rectangle(a1, b1)
area1 = rect1.area()
perimeter1 = rect1.perimeter()
print("The area of first rectangle is :",area1," and perimeter of first rectangle is :",perimeter1)

a2 = int(input("Enter length of the second rectangle: "))
b2 = int(input("Enter breadth of the second rectangle: "))
rect2 = Rectangle(a2, b2)
area2 = rect2.area()
perimeter2 = rect2.perimeter()

if area1 > area2:
    print("\nFirst Rectangle is bigger!")
elif area2 > area1:
    print("\nSecond rectangle is greater!")
else:
    print("\nBoth are equal!")