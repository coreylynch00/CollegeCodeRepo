
import os

for folderName, subfolders, filenames in os.walk('/Users/chima/Documents/test'):
    print('The current folder is '+ folderName)
    
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')




