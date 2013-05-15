import sys, json

def hw():
    print 'Sentiment Analysis'

def lines(fp):
    print str(len(fp.readlines()))
    
def build_model(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def sent_calulate(tweet_file, scores):
    for line in tweet_file:
        result  = json.loads(line)
        if result.has_key('text'):
            #print result['text']
            tweet = result['text']
            words = tweet.split(" ")
            sent_score = 0.0
            for word in words:
                if scores.has_key(word):
                    sent_score += scores[word]
            print sent_score
        else:
            print 0

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    scores = build_model(sent_file)
    sent_calulate(tweet_file, scores)

if __name__ == '__main__':
    main()
