num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("Both numbers are equal")

output:
Enter first number: 5
Enter second number: 8
8.0 is larger than 5.0
