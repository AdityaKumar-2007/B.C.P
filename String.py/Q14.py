A = input()
B = int(input())

ch = chr(B)  
pos = -1

for i in range(len(A)):
    if A[i] == ch:
        pos = i
        break

print(pos)
