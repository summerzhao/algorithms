from __future__ import division
import sys, json

def hw():
    print 'Term Frequent Analysis'

def lines(fp):
    print str(len(fp.readlines()))

def freq_calulate(tweet_file):
    word_freq = {}
    total_word = 0
    for line in tweet_file:
        result  = json.loads(line)
        if result.has_key('text'):
            #print result['text']
            tweet = result['text'].strip()
            words = tweet.split(" ")
            total_word += len(words)
            for word in words:
                if word_freq.has_key(word):
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    for word, count in word_freq.items():
        if len(word.strip()) > 0:
            word = word.strip().encode('utf-8')
            print word, count/total_word

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    freq_calulate(tweet_file)

if __name__ == '__main__':
    main()

