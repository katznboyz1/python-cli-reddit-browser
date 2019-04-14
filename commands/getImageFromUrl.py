import argparse, urllib.request

parser = argparse.ArgumentParser(description = 'A command to convert online images into text.')

parser.add_argument('--url', dest = 'url', required = True)
parser.add_argument('--scale', dest = 'scale', required = False)

args = parser.parse_args()

url = args.url
scale = 1

if (args.scale):
    scale = args.scale

pythonName = str(open('../manifest.txt').read()).split('\n')[0].split('=')[1]

os.system('{} >> ../cache/out.txt'.format(pythonName))