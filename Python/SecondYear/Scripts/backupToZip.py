
#! python3
# backupToZip.py - copy an entire folder and its content into a ZIP file whose name increments

import zipfile, os
def backupToZip(folder):
    folder = os.path.abspath(folder) # make sure folder is absolute path
    # Figure out the file name
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Create the ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s ...' % (foldername))
        # Add the current folder to ZIP file
        backupZip.write(foldername)
        # Add all files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Do not backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
                
    print('Done')
backupToZip('/Users/chima/Documents/test/test2')

