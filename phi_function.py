# Calculates the number of positive integers less than or equal to n that are relatively prime to n

# !! DOES NOT WORK PROPERLY!! LOGIC ERROR
n = 180

count = 1

for num in range(2, n):
    if n % num == 0:
        continue
    count += 1

print(count)
