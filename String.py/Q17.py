A = input()

A = A + A

temp = ""
for ch in A:
    if not (ch >= 'A' and ch <= 'Z'):
        temp = temp + ch

result = ""
v = "aeiou"
for ch in temp:
    if ch in v:
        result = result + "#"
    else:
        result = result + ch

print(result)
