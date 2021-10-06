
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Vincent': 'Mar 27'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is your birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')



