 # elif statement example

print('who are you?')
name = input()
print('What is your age?')
age = int(input())
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, Kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not a Vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

        
