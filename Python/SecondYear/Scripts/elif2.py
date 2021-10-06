 # elif statement example with guaranteed execution

print('who are you?')
name = input()
print('What is your age?')
age = int(input())
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, Kiddo.')
else:
    print('You are neither Alice nor a little kid.')

        
