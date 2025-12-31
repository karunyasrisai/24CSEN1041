year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(f"{year} is a Leap Year")
elif (year % 100 == 0):
    print(f"{year} is NOT a Leap Year")
elif (year % 4 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")

output:
Enter a year: 2022
2022 is NOT a Leap Year
