#python script made for autoinstalling all the required packages for the reddit browser
import os
pythonPath = str(open('./manifest.txt').read()).split('\n')[0].split('=')[1]
requiredModules = ['pillow', 'argparse', 'numpy', 'colorama']
for each in requiredModules:
    os.system('{} -m pip install {}'.format(pythonPath, each))
print ('Done installing the required modules for the reddit browser.')