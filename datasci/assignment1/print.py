import sys, urllib
import json

def crawlTweet():
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
    result  = json.load(response)["results"]
    for i in range(0, len(result)):
        print result[i]['text']


def printTweet(tweet_file):
    #print "in printTweet" 
    for line in tweet_file:
        result  = json.loads(line)
        if result.has_key('text'):
            if result['user']['lang'] == 'en':
                #print result['text']
                tweet = result['text']
                if result['place']:
                    print "place", result['place']
#                print 'geo', result['geo']
#                print 'coordinates', result['coordinates']
#                print 'location', result['user']['location']
#                print 'time zone', result['user']['time_zone']
                    print tweet
                    print 

def main():
    tweet_file = open(sys.argv[1])
    printTweet(tweet_file)
if __name__ == '__main__':
    main()