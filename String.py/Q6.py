A = input()

j = len(A) - 1
while j >= 0 and A[j] == '*':
    j -= 1

result = ""
for i in range(0, j + 1):
    result += A[i]

print(result)
