print("Name : Niranjana S Nair")
print("Roll No: 47")
print("Experiment No: 15")


with open("file.txt", "r") as file:
    lines = [line.strip() for line in file]
    print("lines are:", lines)