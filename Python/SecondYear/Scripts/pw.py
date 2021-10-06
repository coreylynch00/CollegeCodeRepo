
#!/usr/bin/python3
# pw.py - An insecure password locker program

import sys, pyperclip

passwords = {'email': 'F7minlBDDuvMJuXESSKHsid98JKoeisieHH',
             'blog': 'VmALQyKAiH5G3H012alkkdAJKadNadMnntTQ',
             'facebook': 'ggMIsi394FAjad#sioMWroinaD345ios' }
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] ')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)



    
