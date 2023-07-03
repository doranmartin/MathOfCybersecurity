# plaintext
plaintext_string = "Do not eat gas station sushi".lower()
plaintext_string = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

ciphertext = ''

# keys
(s, r) = (3, 10)

for char in plaintext_string:
    plaintext_char = ord(char) - ord('a') + 1
    if char.isalpha():
        ciphertext_char = chr(ord('A') + (s * (plaintext_char + r) % 26))
        ciphertext += ciphertext_char
    else:
        ciphertext += char

print(ciphertext)
