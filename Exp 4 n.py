color_list1=[]
print("Name: Niranjana Sniar")
print("Admision No: A24MCA047")
print(" color list Experiment No: 4")
n=int(input("Enter the limit of colors"))
print("Enter first color list")
for i in range(n):
    c=input("Enter the color")
    color_list1.append(c)
print("color_list1: ",color_list1)
print("The first color : ",color_list1 [0])
print("The last color : ",color_list1[-1])
color_list2=[]
print("Enter second color list")
for i in range(n):
    c=input("Enter the color")
    color_list2.append(c)
print("Color_list 1 not in color_list 2 is ")
uniqueList=[x for x in color_list1 if x not in color_list2]
print(uniqueList)
color_code={
'red': 1, 'green': 2, 'blue' :3, 'yellow':4,
'orange': 5,
'pink':6,
'black':7,
'white': 8,
'purple':9,
}
color_int=[]
for x in color_list1:
    if x in color_code.keys():
        color_int.append(color_code[x])
print("Color code of color_list1", color_int)
oddColor=[x for x in color_int if x%2!=0]
print("Odd colors : ", oddColor)