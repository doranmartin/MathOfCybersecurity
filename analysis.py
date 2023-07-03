num = -1
num2 = 7

for x in range(0, 100):
    num += 26
    if num % num2 == 0:
        print(num, num / num2)
