A = input()

i = 0
while i < len(A) and A[i] == '*':
    i += 1

result = ""
for k in range(i, len(A)):
    result += A[k]

print(result)
