#python script made for autoinstalling all the required packages for the reddit browser
import os
pythonPath = str(input('Python Name (python, py.exe, python3 [...]): '))
requiredModules = ['pillow', 'argparse', 'numpy']
for each in requiredModules:
    os.system('{} -m pip install {}'.format(pythonPath, each))
print ('Done installing the required modules for the reddit browser.')