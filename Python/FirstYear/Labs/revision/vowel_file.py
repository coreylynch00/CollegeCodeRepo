
vowels = ('a', 'e', 'i', 'o', 'u')
data = open("vowel.txt")

for word in data:
    word = word.rstrip()
    for letter in word:
        if letter not in vowels:
            print(letter, end="")
    print()
data.close()
