# Finds x such that -> a * x == b (mod n)

a = 6
b = 1
n = 55

for x in range(1000):
    if a * x % n == b:
        print(x)
        break


# for x in range(1000):
#     if (28 * x + 40) % 26 == 18:
#         print(x)
#         break
