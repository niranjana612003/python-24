print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 3")

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.Area=0

    def area(self):
        self.Area = self.length * self.breadth
        return self.Area

    def __lt__(self, other):
        if r1.Area > r2.Area:
            print("The first rectangle has more area!")
        elif r1.Area < r2.Area:
            print("The second rectangle has more area!")
        else:
            print("Both rectangles have same area!")

l1 = int(input("Enter the length : "))
b1 = int(input("Enter the breadth : "))
r1 = Rectangle(l1,b1)
print(f"The area of first rectangle is : {r1.area()}")

l2 = int(input("\nEnter the length : "))
b2 = int(input("Enter the breadth : "))
r2 = Rectangle(l2,b2)
print(f"The area of second rectangle is : {r2.area()}\n")

r1<r2
