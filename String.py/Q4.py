A = input()

s = 0
while s < len(A) and A[s] == '*':
    s += 1

e = len(A) - 1
while e >= 0 and A[e] == '*':
    e -= 1

ans = ""
for i in range(s, e + 1):
    ans += A[i]

print(ans)

