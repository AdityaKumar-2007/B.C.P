A = int(input("Enter an integer A: "))
A_str = str(A)
if A_str == A_str[::-1]:
    print("Yes  plaindrome")
else:
    print("Not a plaindrome")
