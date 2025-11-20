A = input()
B = input()

pos = -1

for i in range(len(A) - len(B) + 1):
    match = True
    for j in range(len(B)):
        if A[i + j] != B[j]:
            match = False
            break
    if match:
        pos = i
        break

print(pos)
