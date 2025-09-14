N = int(input("Enter an integer N: "))
digit_sum = 0
N = abs(N)
while N > 0:
    digit_sum += N % 10
    N //= 10
print(digit_sum)
