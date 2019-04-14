import os
os.chdir('./commands') #set the directory to the commands folder
pythonName = str(input('What is the name of your python command (py.exe, py, python, python3, [...]): ')) #check what python they are using
print ('Type "help.py" for a full list of commands and other help info.')
while (True):
    command = str(input('Reddit CLI Browser> ')) #command input
    if (command == 'exit'):
        break
    else:
        if (command.split(' ')[0] in os.listdir('.')):
            os.system('{} {}'.format(pythonName, command)) #run the designated python script
        else:
            print ('Unknown command. Type "help.py" for a full list of commands.')