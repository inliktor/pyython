import os
import fnmatch
import shutil
path=r"C:\Users\Liktor\Desktop"
desktop=os.chdir(path)
s=os.getcwd()
print('______________\n')
print(s)
print('______________\n')
for root, dir, files in os.walk(r'C:/Users/Public/'):
    for name in files:
        print(name)
        for name in os.listdir('.'):
            if fnmatch.fnmatch(name, '*.'):

                print(name)
            
        #fullname = os.path.join(root, name)
        #print(fullname)
