
# add tools for monoalphabetic ciphers :)

plain = ord('t') - ord('a') + 1
cipher = ord('J') - ord('A') + 1

s = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

print(plain, cipher)
seed = 0

for num in s:
  if cipher == plain * num % 26:
    seed = num
    print(num)

new_plain = ord('c') - ord('a') + 1

print(seed * new_plain % 26)
