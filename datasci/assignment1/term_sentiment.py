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
    absent_word = {}
    for line in tweet_file:
        result  = json.loads(line)
        if result.has_key('text'):
            #print result['text']
            tweet = result['text']
            words = tweet.split(" ")
            sent_score = 0.0
            wordlist = []
            for word in words:
                if scores.has_key(word):
                    sent_score += scores[word]
                else:
                    wordlist.append(word)  
            for word in wordlist:
                #print word
                if absent_word.has_key(word):
                    absent_word[word] += sent_score
                else:
                    absent_word[word] = sent_score
            #print sent_score
        #else:
            #print 0
    for word, score in absent_word.items():
        if len(word.strip()) > 0:
            word = word.strip().encode('utf-8')
            print word, score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    scores = build_model(sent_file)
    sent_calulate(tweet_file, scores)

if __name__ == '__main__':
    main()

