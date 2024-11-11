print("Niranjana S Nair")
print("Admission No: A24MCA047")
print("Date and leap year Experiment: 1")
Day=int(input("enter the day"))
Month=int(input(" enter the month"))
Year=int(input("enter the year"))
print("date is:",Day,"/",Month,"/",Year)

if(Year % 4 == 0) and (Year % 100 != 0):
        print("leap year")
else:
        print("not leap year")