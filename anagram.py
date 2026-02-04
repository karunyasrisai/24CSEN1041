s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an anagram")

OUTPUT:
Enter first string: earth
Enter second string: heart
Anagram
