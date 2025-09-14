numbers = [1, 3, 5]
for i in range(1, 6):
    if i == 1:
        print("1")
    else:
        line = []
        count = 0
        for num in numbers:
            line.append(str(num))
            count += 1
            if count == (i + 1) // 2:
                break
        print(' * '.join(line))
