print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 1")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare(self, other):
        if self.area() > other.area():
            print("Area of 1st rectangle is greater than 2nd rectangle")
        elif self.area() < other.area():
            print("Area of 2nd rectangle is greater than 1st rectangle")
        else:
            print("Area of 1st and 2nd rectangle are equal")


def get_rectangle_input(number):
    while True:
        try:
            length = int(input(f"Enter length of {number} rectangle: "))
            width = int(input(f"Enter width of {number} rectangle: "))
            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive integers.")
            return length, width
        except ValueError as ve:
            print(f"Invalid input. {ve}. Please enter valid integers.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


print("---1st Rectangle---")
length, width = get_rectangle_input("1st")
obj1 = Rectangle(length, width)
print(f"Area = {obj1.area()}")
print(f"Perimeter = {obj1.perimeter()}")

print("---2nd Rectangle---")
length1, width1 = get_rectangle_input("2nd")
obj2 = Rectangle(length1, width1)
print(f"Area = {obj2.area()}")
print(f"Perimeter = {obj2.perimeter()}")

obj1.compare(obj2)