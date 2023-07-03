# Finds x such that -> a * x == 1 (mod n)

a = 15
b = 25
n = 100

for x in range(1000):
    if a * x % n == b:
        print(x)
        # break
