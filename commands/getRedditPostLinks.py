#make it so that it can get posts after a certain amount

import argparse, urllib.request, json

parser = argparse.ArgumentParser(description = 'A program that will get a list of reddit posts on a certain page.')

parser.add_argument('--subreddit', dest = 'subreddit', required = True)
parser.add_argument('--limit', dest = 'limit', required = False)
parser.add_argument('--after', dest = 'after', required = False)

args = parser.parse_args()

subreddit = args.subreddit
limit = 10 - 1
if (args.limit):
    limit = int(args.limit) - 1
after = 0
if (args.after):
    after = args.after

redditData = urllib.request.urlopen('https://www.reddit.com/r/{}/.json?limit={}&after={}'.format(subreddit, limit, after))
redditData = json.loads(redditData.read().decode())

redditData = redditData['data']['children']

print ('-------------------------------------------------------------------------------')

print ('Showing {} posts from r/{}:'.format(limit, subreddit))

for post in range(len(redditData)):
    title = redditData[post]['data']['title']
    url = redditData[post]['data']['url']
    upvotes = redditData[post]['data']['score']
    try:
        print ('\n{} - {}\n{} upvotes'.format(title, url, str(upvotes)))
    except:
        print ('\nError printing this title. It probably had an emoji in it.')

print ('-------------------------------------------------------------------------------')