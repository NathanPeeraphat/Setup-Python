for i in range(1, 13):
    double = i * 2
    print(double)

for i in range(1, 13):
    if i % 3 == 0:
        continue
    print(i)

for i in range(1, 13):
    if i % 3 == 0:
        break
    print(i)