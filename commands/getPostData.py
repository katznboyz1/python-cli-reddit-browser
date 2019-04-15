import argparse, urllib.request, json, os

pythonName = str(open('../manifest.txt').read()).split('\n')[0].split('=')[1]

parser = argparse.ArgumentParser(description = 'A program that gets the data from a reddit post URL. This only works with reddit post URL\'s.')

parser.add_argument('--url', dest = 'url', required = True)
parser.add_argument('--showmedia', dest = 'showmedia', required = False)
parser.add_argument('--mediascale', dest = 'mediascale', required = False)

args = parser.parse_args()

showmedia = 'n'
if (args.showmedia):
    showmedia = args.showmedia.lower()
if (showmedia not in ['y', 'n']):
    print ('--showmedia must be a (y,n) value.')
    exit()

mediascale = '1'
if (args.mediascale):
    mediascale = args.mediascale

url = args.url

try:
    redditData = urllib.request.urlopen('{}/.json'.format(url))
except urllib.error.HTTPError as err:
    print ('429 HTTP Error, try waiting for a little bit and then using this command again. Usually you can just wait three seconds and then it will work again.')
    exit()

redditData = json.loads(redditData.read().decode())
redditData = redditData[0]['data']['children'][0]['data']

mediaURL = redditData['url']
title = redditData['title']
author = redditData['author']
score = redditData['score']
comments = redditData['num_comments']
isSelftext = redditData['is_self']
selfText = redditData['selftext']

print ('')
print ('Title: {}'.format(title))

if (showmedia == 'y' and isSelftext == False):
    os.system('{} getImageFromUrl.py --url {} --scale {}'.format(pythonName, mediaURL, mediascale))

if (isSelftext):
    print ('Selftext: {}'.format(selfText))

print ('\n{} upvotes | {} comments | uploaded by u/{}\n'.format(score, comments, author))