from __future__ import division
import sys, json, operator

def hw():
    print 'Term Frequent Analysis'

def lines(fp):
    print str(len(fp.readlines()))

def freq_calulate(tweet_file):
    word_freq = {}
    for line in tweet_file:
        result  = json.loads(line)
        if result.has_key('entities'):
            #print result['text']
            hashtags = result['entities']['hashtags']
            for tag in hashtags:
                tag_text = tag['text']
                if word_freq.has_key(tag_text):
                    word_freq[tag_text] += 1
                else:
                    word_freq[tag_text] = 1
    sorted_word_freq = sorted(word_freq.iteritems(), key=operator.itemgetter(1))
    sorted_word_freq.reverse()
    index = 0;
    for word, count in sorted_word_freq:
        if index < 10:
            if len(word.strip()) > 0:
                word = word.strip().encode('utf-8')
                print word, count
                index += 1
        else:
            break

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    freq_calulate(tweet_file)

if __name__ == '__main__':
    main()

