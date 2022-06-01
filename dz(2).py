from codecs import ignore_errors
import os
import fnmatch
# импортировали ;D я постараюсь сделать код читаемым 
s=os.getcwd
print('______________\n')
print('щас мы узнаем что ты слушаешь !!!')
print('______________\n')
print('проверяем наличие папки музыка')
print('______________\n')
path=r'C:\Users\Liktor\Desktop\музыка'

if(os.path.exists(r'Desktop/музыка')):
    print('папка музыка существует')
else:
    print('папки музыка не существует')
print('______________\n')
print('план скам')
print('______________\n')
try:
    for dirs,folder,files in os.walk(path):
        print('Выбранный каталог: ', dirs)
        print('Вложенные папки: ', folder)
        print('Файлы в папке: ', files)
        print('Полный путь к файлу: ', os.path.join(dirs, folder))
except:
    ignore_errors
print('______________\n')
for root, dirs, files in os.walk(r'C:\Users\Liktor\Desktop\музыка'):
    for name in files:
        #print(root)
        #print(name)
        fullname = os.path.join(root, name)
        print(fullname)
print('______________\n')
#ел если будешь читать это то удачи я буду делать 3 мейби подумаю