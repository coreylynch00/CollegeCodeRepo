valid_answers = ('yes', 'no', 'y', 'n')

while True:
    answer = input("Are you ready? ").lower()
    if answer in valid_answers:
        break

if answer == 'no' or answer == 'n':
    print("Well then, stay at home!")
else:
    print("Let's get started...")



