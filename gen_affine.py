# plaintext
plaintext_string = "Do not eat gas station sushi".lower()
plaintext = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

# keys
(s, r) = (3, 10)

for char in plaintext_string:
    plaintext_char = ord(char) - ord('a') + 1
    ciphertext_char = chr(ord('A') + (s * (plaintext_char + r) % 26))
    print(ciphertext_char)
