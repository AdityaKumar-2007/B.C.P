A = int(input("Enter a positive integer A: "))
odd_sum = 0
for i in range(1, A + 1, 2):
    odd_sum += i
print(odd_sum)
