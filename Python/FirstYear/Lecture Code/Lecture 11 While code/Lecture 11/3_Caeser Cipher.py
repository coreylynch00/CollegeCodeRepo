message = input("Please type a word/phrase >>> ")
numberOfChars = len(message)
i = 0
encoded = ""
while i < numberOfChars:
    if message[i].isalpha():
        if message[i] == 'z':
            encoded += 'a'
        elif message[i] == 'Z':
            encoded += 'A'
        else:
            ascii_code = ord(message[i])
            ascii_code = ascii_code + 1
            letter = chr(ascii_code)
            encoded += letter
    else:
        encoded += message[i]
    i += 1

print("Original:", message)
print("Encrypted:", encoded)