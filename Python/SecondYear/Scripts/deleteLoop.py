
import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)



'''import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)'''
