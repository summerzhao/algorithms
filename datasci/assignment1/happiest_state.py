import sys, json, operator

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
    states = {}
    for line in tweet_file:
        result  = json.loads(line.encode('utf-8'))
        if result.has_key('text') and result['user']['lang'] == 'en' and result['place']:
            state = result['place']['full_name']
            if state:
                #print state
                state = state.encode('utf-8')
                splits = state.split(',')
                if len(splits) > 1:
                    state = splits[1].strip()
                    #print state
                    if len(state) == 2:
                        tweet = result['text']
                        words = tweet.split(" ")
                        sent_score = 0.0
                        for word in words:
                            if scores.has_key(word):
                                sent_score += scores[word]
                        if states.has_key(state):
                            states[state] += sent_score
                        else:
                            states[state] = sent_score
            #print sent_score
    sorted_states = sorted(states.iteritems(), key=operator.itemgetter(1))
    sorted_states.reverse()
    index = 0;
    for word, count in sorted_states:
        if index < 1:
            if len(word.strip()) > 0:
                word = word.strip().encode('utf-8')
                print word
                index += 1
        else:
            break
            

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    scores = build_model(sent_file)
    sent_calulate(tweet_file, scores)

if __name__ == '__main__':
    main()
