print("Niranjana S Nair")
print("Admission No: A24MCA047")
print("greatest,area,perimeter,volume Experiment: 3")

a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
if a>b:
      if a>c:
          print(a,"greatest")
          n = a
else:
          print(c,"greatest")
n = c

if b>c:
         print(b,"greatest")
         n = b

else:
    print(c,"greatest")
    n = c

nn =int(f"{n}{n}")
nnn =int(f"{n}{n}{n}")
result= n+nn+nnn
print("result of n+nn+nnn:",result)
area = 3.14*n*n
perimeter = 2*3.14*n
volume = (4/3)*3.14*(n*n*n)

print(" area of the circle with radius",n,"is",area)
print(" perimeter of the circle with radius", n, "is", perimeter)
print("volume of the sphere:",n,volume)
