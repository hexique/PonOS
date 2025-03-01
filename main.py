# main.py

from time import sleep, ctime
from inspect import signature

__version__ = 'a1.1.2'
__date__ = '28.02.2025'

audit = ''

directoryList = {
    'root': {
        'os': {
            'help.txt': 'just a help menu'},
        'prg': {
            'text.txt': 'text file',
            'hello.py': 'print("Hello World!")'
            }
        },
}


current_path = []

def cowsay(text):
    print(f'''
 _{"_" * len(text)}_
< {text} >
 -{"-" * len(text)}-
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
''')

def goto(path):
    global directoryList, current_path, audit

    parts = path.split('/')
    temp_path = current_path.copy()

    for part in parts:
        if part == '..':
            if len(temp_path) > 0:
                temp_path.pop()
        elif part == '.':
            continue
        else:
            current_level = directoryList
            for p in temp_path:
                current_level = current_level[p]

            if '.' in part and part.split('.')[0] and part.split('.')[1]:
                if part not in current_level:
                    current_level[part] = ''
                    print(f"Created file '{part}'")
                else:
                    while True:
                        print(f"'{part}'")
                        print(current_level[part])
                        new_content = input(f"Write new value of file '{part}'\n")
                        audit += new_content
                        if new_content:
                            if new_content.startswith('-w'):
                                current_level[part] = new_content[3::]
                            elif new_content.startswith('-a'):
                                current_level[part] += new_content[3::]
                            elif new_content.startswith('-d'):
                                if input(f"Are you sure you want delete file '{part}'? (y/n)\n") == 'n':
                                    continue
                                else:
                                    current_level.pop(part)
                                    print(f"File '{part}' deleted.")
                                    return
                            elif new_content.startswith('-r'):
                                current_level[part] = current_level[part][::int(new_content[3::])]
                            elif new_content.startswith('-e'):
                                return
                        print(f"New value of file '{part}':\n{current_level[part]}")
                return

            if part not in current_level:
                current_level[part] = {}

            temp_path.append(part)

    current_path = temp_path

def tree():
    print(directoryList)

def ctree():
    temp_path = directoryList
    for i in current_path:
        try:
            temp_path = temp_path[i]
        except KeyError:
            print(f"This directory is empty.")
            return
    print('; '.join(list(temp_path.keys())))

def comp(path):
    global directoryList, current_path, audit

    parts = path.split('/')
    temp_path = current_path.copy()

    for part in parts:
        if part == '..':
            if len(temp_path) > 0:
                temp_path.pop()
        elif part == '.':
            continue
        else:
            current_level = directoryList
            for p in temp_path:
                current_level = current_level[p]

            if '.' in part and part.split('.')[0] and part.split('.')[1]:
                if part not in current_level:
                    print(f"File '{part}' doesn't exist")
                else:
                    while True:
                        exec(current_level[part], globals())
                        return
                return

            temp_path.append(part)

    current_path = temp_path

def getvar(var):
    print(f'{globals()[var]}')

commandList = {
    'cowsay': cowsay,
    'comp': comp,
    'ctree': ctree,
    'date': lambda: print(f'Today is {ctime()}'),
    'goto': goto,
    'tree': tree,
    '--': getvar,
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
    print(f"{'/'.join(current_path)}", end=' ')
    command = input()
    if len(signature(commandList[command.split(' ')[0]]).parameters) == 0:
        commandList[command.split(' ')[0]]()
    elif len(signature(commandList[command.split(' ')[0]]).parameters) == 1:
        commandList[command.split(' ')[0]](' '.join(command.split(' ')[1::]))
    elif len(signature(commandList[command.split(' ')[0]]).parameters) == 2:
        commandList[command.split(' ')[0]](' '.join(command.split(' ')[1]), ' '.join(command.split(' ')[2::]))