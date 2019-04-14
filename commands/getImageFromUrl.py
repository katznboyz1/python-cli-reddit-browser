import argparse, urllib.request

parser = argparse.ArgumentParser(description = 'A command to convert online images into text.')

parser.add_argument('--url', dest = 'url', required = True)
parser.add_argument('--scale', dest = 'scale', required = False)

args = parser.parse_args()
