i = 1

while i in range(1000):
    if i % 3 == 0:
        print(i)
        i = i + 1
    else:
        i = i + 1
        continue