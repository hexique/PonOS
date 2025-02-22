# main.py

from time import sleep, ctime
from inspect import signature

__version__ = 'a1.0'
__date__ = '22.02.2025'
def cowsay(text):
    print(f'''
 _{"_" * len(text)}_
/ {text} /
 -{"-" * len(text)}-
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
''')

commandList = {
    'cowsay': cowsay,
    'date': lambda: print(f'Today is {ctime()}'),
    'version': lambda: print(f'{__version__} {__date__}'),
}



for i in range(0,7):
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
    elif len(signature(commandList[command.split(' ')[0]]).parameters) == 1:
        commandList[command.split(' ')[0]](' '.join(command.split(' ')[1]), ' '.join(command.split(' ')[1::]))

