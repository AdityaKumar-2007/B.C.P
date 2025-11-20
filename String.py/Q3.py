t = int(input())
for i in range(t):
    s = input().strip()
    if s == s[::-1]:
        print(1)
    else:
        print(0)
 