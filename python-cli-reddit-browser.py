#made by katznboyz/katznboyz1
import os, colorama
os.chdir('./commands') #set the directory to the commands folder
pythonName = str(open('../manifest.txt').read()).split('\n')[0].split('=')[1]
print ('Type "help.py" for a full list of commands and other help info.')
while (True):
    command = str(input('\nReddit CLI Browser> ')) #command input
    if (command == 'exit'):
        break
    else:
        if (command.split(' ')[0] in os.listdir('.')):
            os.system('{} {}'.format(pythonName, command)) #run the designated python script
        else:
            print ('Unknown command. Type "help.py" for a full list of commands.')
