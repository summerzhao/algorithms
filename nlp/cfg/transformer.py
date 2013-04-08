'''
Created on Apr 8, 2013

@author: stefaniezhao
'''
import sys, json
from collections import defaultdict

threshold = 5
rare_label = "_RARE_"

def word_counts(counts, tree):
    if len(tree) == 3:
        # It is a binary rule. Recursively count the children.
        word_counts(counts, tree[1])
        word_counts(counts, tree[2])
    elif len(tree) == 2:
        # It is a unary rule.
        counts[tree[1]] += 1
        
def correct(counts, tree):
    if len(tree) == 3:
        # It is a binary rule. Recursively count the children.
        correct(counts, tree[1])
        correct(counts, tree[2])
    elif len(tree) == 2:
        # It is a unary rule.
        word = tree[1]
        #print word, counts[word]
        if counts[word] < threshold:
            tree[1] = rare_label
            #print tree[1]
    
def main(parse_file):
    counts = defaultdict(int)
    input = open(parse_file)
    for l in input:
        t = json.loads(l)
        word_counts(counts, t)
    #print counts
    input.seek(0,0)
    for l in input:
        t = json.loads(l)
        #print "ord-tree", t
        correct(counts, t)
        print json.dumps(t)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    main(sys.argv[1])