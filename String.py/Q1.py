t = int(input())
for _ in range(t):
    s = input().strip()
    vowels = 0
    consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    print(vowels, consonants)
