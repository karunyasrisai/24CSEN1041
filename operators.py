a = 22
b = 56


print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.3f}")   
print(f"{a} % {b} = {a % b}\n")


print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")


print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")


print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")


print("\n" + ("a is greater than b" if a > b else "b is less than a"))

Output:
Arithmetic Operators
22 + 56 = 78
22 - 56 = -34
22 * 56 = 1232
22 / 56 = 0.393
22 % 56 = 22

Relational Operators
22 < 56 = True
22 > 56 = False
22 == 56 = False
22 != 56 = True

Logical Operators
AND 22 and 56 = True
OR 22 or 56 = True
NOT 22 = False

Bitwise Operators
22 & 56 = 16
22 | 56 = 62
Bitwise XOR 22 ^ 56 = 46
Left Shift 22 << 2 = 88
Right Shift 22 >> 2 = 5

b is less than a

=== Code Execution Successful ===
