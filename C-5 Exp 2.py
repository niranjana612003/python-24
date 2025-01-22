print("Name : Niranjana S Nair")
print("Roll No: 47")
print("Experiment No: 16")

with open("file.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line_number, line in enumerate(infile, start=1):
        if line_number % 2 != 0:
            outfile.write(line)


print("Odd lines have been copied from Input.txt to Output.txt are:")

with open("output.txt", "r") as outfile:
    output = outfile.read()
    print(output)