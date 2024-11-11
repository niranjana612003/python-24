print("Name : Niranjana S Nair")
print("Admission no : A24MCA047")
print("Experiment no : 3")
def factor(n):
    return [i for i in range(1, n + 1) if n % i == 0]
num=int(input("Enter a number : "))
print(factor(num))

side=int(input("Enter the side : "))
area1=lambda side:side**2
print("Area of Square : ",area1(side))

length=int(input("Enter the length : "))
breadth=int(input("Enter the breadth : "))
area2=lambda length,breadth:length * breadth
print("Area of Rectangle : ",area2(length,breadth))

base=int(input("Enter the base : "))
height=int(input("Enter the height : "))
area3=lambda base ,height:.5 * base * height
print("Area of Triangle : ",area3(base,height))