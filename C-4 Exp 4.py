print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 3")

class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total_seconds = (self.__hour * 3600 + self.__minute * 60 + self.__second) + \
                        (other.__hour * 3600 + other.__minute * 60 + other.__second)

        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60

        return Time(hour, minute, second)

    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

h1 = int(input("Enter hours for the first time: "))
m1 = int(input("Enter minutes for the first time: "))
s1 = int(input("Enter seconds for the first time: "))
t1 = Time(h1, m1, s1)
print("First time: ")
t1.display()

h2 = int(input("\nEnter hours for the second time: "))
m2 = int(input("Enter minutes for the second time: "))
s2 = int(input("Enter seconds for the second time: "))
t2 = Time(h2, m2, s2)
print("Second time: ")
t2.display()

t3 = t1 + t2
print("\nSum of the two times: ")
t3.display()