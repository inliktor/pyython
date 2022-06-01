import os
import fnmatch
import shutil
path=r"C:\Users\Liktor\Desktop"
desktop=os.chdir(path)
s=os.getcwd()
print('______________\n')
print(s)
print('______________\n')
for root, dirs, files in os.walk(path):
    print(files)
for name in files:
    for name in os.listdir('.'):
        if fnmatch.fnmatch(name, '*.'):
                print(name)
            
        #fullname = os.path.join(root, name)
        #print(fullname)
