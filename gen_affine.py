# plaintext
plaintext_string = "graph"

# keys
(s, r) = (7, 10)

for char in plaintext_string:
    plaintext_char = ord(char) - ord('a') + 1
    ciphertext_char = chr(ord('A') + (s * (plaintext_char + r) % 26))
    print(ciphertext_char)
