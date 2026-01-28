first_num = int(input("Enter the first num:"))
second_num = int(input("Enter the second num:"))
break_num = int(input("Enter the valid num:"))

for i in range(first_num, second_num):
    if i % 2 == 0:
        continue 
    elif i == break_num:
        break    
    else:
        pass      

    print(i)

OUTPUT:
Enter the first num:6
Enter the second num:50
Enter the valid num:43
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49

=== Code Execution Successful ===
