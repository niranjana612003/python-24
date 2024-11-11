print("Niranjana S Nair")
print("Admission no : A24MCA047 ")
print("Factorial and Fibonacci number Experiment : 1")
import math
num = int(input("Enter a number : "))
print("Factorial :",math.factorial(num))
n = int(input("Enter the Limit : "))
n1 = 0
n2 = 0
i = 0
j = 0
s = 1
print("Fibonacci series :")
while i < n :
    print(n1)
    if j < n :
        n2 = n2 + n1
    n3 = n1 + s
    n1 = s
    s = n3
    i = i + 1
print("Sum is : ",n2)
sqlist =[]
for i in range(1000,10000):
    sq_nm = math.sqrt(i)
    if sq_nm.is_integer():
        n=i
        flag = True
        while n != 0:
            r = n % 10
            if r % 2 != 0:
                flag = False
                break
            n = n // 10
        if flag:
            sqlist.append(i)
print("The list of perfect square 4 digits are : ",sqlist)



