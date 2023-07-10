a = 17
b = -3
c = 5

for e in range(100):
    if (a * e + b) % 26 == c:
        print(e)
        break
