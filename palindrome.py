def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("madam"))      
print(is_palindrome("python"))      
print(is_palindrome("nurses run"))  

OUTPUT:
True
False
True
