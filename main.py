# main.py

from time import sleep, ctime
from inspect import signature

__version__ = 'a1.0.1'
__date__ = '22.02.2025'

directoryList = {
    'root': {
        'ponos': {
            'help.txt': '''just a help menu''', 
            },
    },
}

# Глобальная переменная для хранения текущего пути
current_path = ['root']

def cowsay(text):
    print(f'''
 _{"_" * len(text)}_
| {text} |
 -{"-" * len(text)}-
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
''')

def cd(path):
    global directoryList, current_path

    parts = path.split('/')
    temp_path = current_path.copy()

    for part in parts:
        if part == '..':
            if len(temp_path) > 1:
                temp_path.pop()
        elif part == '.':
            continue
        else:
            # Получаем текущий уровень
            current_level = directoryList
            for p in temp_path:
                current_level = current_level[p]

            # Если директория не существует, создаем её
            if part not in current_level:
                if len(parts[-1].split('.')) != 0:
                    current_level[part] = ''
                    return
                current_level[part] = {}

            temp_path.append(part)

    # Обновляем текущий путь
    current_path = temp_path

    print(f"{'/'.join(current_path)}", end=' ')

def tree():
    print(directoryList)

commandList = {
    'cd': cd,
    'cowsay': cowsay,
    'date': lambda: print(f'Today is {ctime()}'),
    'tree': tree,
    'version': lambda: print(f'{__version__} {__date__}'),
}

for i in range(0, 7):
    print(f'''                            
     Welcome to the...        
                            
PPP              OOO   SSS  
P  P            O   O S     
P  P  oo  n nn  O   O  SS   
PPP  o  o nn  n O   O    S  
P    o  o n   n O   O    S  
P     oo  n   n  OOO  SSS   
                            
{__version__} {__date__}
'''.replace(' ', ('@', '#', '?', '/', '-', '.', ' ')[i]))
    sleep(0.1)

while True:
    command = input()
    if len(signature(commandList[command.split(' ')[0]]).parameters) == 0:
        commandList[command.split(' ')[0]]()
    elif len(signature(commandList[command.split(' ')[0]]).parameters) == 1:
        commandList[command.split(' ')[0]](' '.join(command.split(' ')[1::]))
    elif len(signature(commandList[command.split(' ')[0]]).parameters) == 2:
        commandList[command.split(' ')[0]](' '.join(command.split(' ')[1]), ' '.join(command.split(' ')[2::]))