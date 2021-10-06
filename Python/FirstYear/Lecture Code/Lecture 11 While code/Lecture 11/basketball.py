sport = "basketball"
i = 0
while i < len(sport):
    print(sport[i], end='*')
    if sport[i] in vowels:
        number_of_vowels += 1
    i += 1