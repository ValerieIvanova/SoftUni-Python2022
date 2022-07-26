text = input()
encrypted_text = ''
for char in text:
    numeric_value = ord(char) + 3
    encrypted_text += chr(numeric_value)
print(encrypted_text)