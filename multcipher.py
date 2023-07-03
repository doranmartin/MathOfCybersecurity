# Encrypts message using additive cipher

plaintext = "Do not eat gas station sushi".lower()
plaintext = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

s = 23

ciphertext = ''

a = ord('a')
z = ord('z')

for char in plaintext:
    if char.isalpha():
        char = s * (ord(char) - a + 1) % 26 + a - 1
        print(char)
        ciphertext += chr(char)
    else:
        ciphertext += char

print(ciphertext.upper())
