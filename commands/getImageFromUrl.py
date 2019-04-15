import argparse, urllib.request, os

parser = argparse.ArgumentParser(description = 'A command to convert online images into text.')

parser.add_argument('--url', dest = 'url', required = True)
parser.add_argument('--scale', dest = 'scale', required = False)

args = parser.parse_args()

url = args.url
scale = 1

if (args.scale):
    scale = args.scale

if ('cache' not in os.listdir('..')):
    os.mkdir('../cache')

pythonName = str(open('../manifest.txt').read()).split('\n')[0].split('=')[1]

imageFilePath = '../cache/tmpImage1.' + args.url.split('.')[-1]

urllib.request.urlretrieve(url, imageFilePath)

os.system('{} imageToText.py --file {} --scale {} --out ../cache/asciiImageOutput.txt >> ../cache/out.txt'.format(pythonName, imageFilePath, scale))

print (str(open('../cache/asciiImageOutput.txt').read()))

os.remove(imageFilePath)
os.remove('../cache/asciiImageOutput.txt')