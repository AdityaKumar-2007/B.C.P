def print_down(n):
    if n == 0:
        return
    print(n, end=" ")
    print_down(n - 1)

n = int(input())
print_down(n)
