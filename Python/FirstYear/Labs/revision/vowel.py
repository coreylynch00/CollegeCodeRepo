vowels = ('a', 'e', 'i', 'o', 'u')
word = input("Word >>>")

while word != "":
    for letter in word:
        if letter not in vowels:
            print(letter, end="")
    print()
    word = input("Word >>>")
