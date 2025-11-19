def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pal(s[1:-1])

s = input()
print("Palindrome" if is_pal(s) else "Not Palindrome")
