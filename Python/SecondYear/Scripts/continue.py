# example continue statement

while True:
    print('Who are you?')
    name = input()
    if name != 'Vincent':
        continue
    print('Hello, Vincent. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
