# Encrypts message using additive cipher

plaintext = "Do not eat gas station sushi"
plaintext = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

r = 11

ciphertext = ''

a = ord('a')
z = ord('z')

for char in plaintext:
    if char.isalpha():
        char = ord(char) + r
        if char >= z:
            char = char % z + a 
        ciphertext += chr(char)
    else:
        ciphertext += char

print(ciphertext.upper())
