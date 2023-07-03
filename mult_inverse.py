# Finds x such that -> a * x == b (mod n)

a = 7
b = 1
n = 26

for x in range(1000):
    if a * x % n == b:
        print(x)
        break
