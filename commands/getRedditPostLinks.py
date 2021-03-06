#made by katznboyz/katznboyz1
#make it so that it can get posts after a certain amount

import argparse, urllib.request, json, urllib

parser = argparse.ArgumentParser(description = 'A program that will get a list of reddit posts on a certain page.')

parser.add_argument('--subreddit', dest = 'subreddit', required = True)
parser.add_argument('--limit', dest = 'limit', required = False)
parser.add_argument('--after', dest = 'after', required = False)
parser.add_argument('--sortby', dest = 'sortby', required = False)

args = parser.parse_args()

subreddit = args.subreddit
limit = 10 - 1
if (args.limit):
    limit = int(args.limit) - 1
after = 0
if (args.after):
    after = args.after
sortby = 'new'
if (args.sortby):
    if (args.sortby.lower() in ['new', 'hot', 'rising', 'top', 'controversial']):
        sortby = args.sortby
    else:
        print ('--sortby must be one of the following values: new, hot, rising, top, controversial')

try:
    redditData = urllib.request.urlopen('https://www.reddit.com/r/{}/{}/.json?limit={}&after={}'.format(subreddit, sortby, limit, after))
except urllib.error.HTTPError as err:
    print ('429 HTTP Error, try waiting for a little bit and then using this command again. Usually you can just wait three seconds and then it will work again.')
    exit()

redditData = json.loads(redditData.read().decode())

redditData = redditData['data']['children']

print ('-------------------------------------------------------------------------------')

print ('Showing {} posts from r/{}:'.format(str(int(limit) + 1), subreddit))

for post in range(len(redditData)):
    title = redditData[post]['data']['title']
    url = redditData[post]['data']['permalink']
    upvotes = redditData[post]['data']['score']
    comments = redditData[post]['data']['num_comments']
    uploader = redditData[post]['data']['author']
    try:
        print ('''
Title: {}
URL: https://www.reddit.com{}
Upvotes: {}
Comments: {}
Uploader: u/{}
'''.format(title, url, upvotes, comments, uploader))
    except:
        print ('\nError printing this title. It probably had an emoji in it.')

print ('-------------------------------------------------------------------------------')
