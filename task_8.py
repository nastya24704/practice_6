t = int(input())
numbers = []
for i in range (0, 10):
    numbers.append (i)
for a in range (10, 100):
    numbers.append (a // 10)
    numbers.append (a % 10)
for b in range (100, 201):
    numbers.append ((b // 10) // 10)
    numbers.append ((b // 10) % 10)
    numbers.append (b % 10)
k = numbers[t-1]
print(k)
