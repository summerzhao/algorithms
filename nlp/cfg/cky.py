'''
Created on Apr 8, 2013

@author: stefaniezhao
'''
from count_cfg_freq import Counts
import sys, json

rare_label = "_RARE_"

class CKY(object):
    
    def __init__(self):
        self.counter = None
    
    def load_params(self, input):
        self.counter = Counts() 
        self.counter.load(open(input))
        
    def cky(self, test_file):
        for line in test_file:
            self.parse(line)
            
    def constract_result(self, tp, words, i, j, N):
        #print t[(1, n, "S")]
        tree = []
        tree.append(N)
        if i == j:
            tree.append(words[i-1])
            return tree
        else:
            (s, Y, Z) = tp[(i, j, N)]
            #print s, Y, Z
            tree.append(self.constract_result(tp, words, i, s, Y))
            tree.append(self.constract_result(tp, words, s+1, j, Z))
            return tree

    def parse(self, line):
        t = {}
        tp = {}
        #init
        words = line.strip().split(" ")
        n = len(words)
        #print words
        i = 1
        for word in words:
            if self.counter.unary_pob_reorg.has_key(word):
                for N, freq in self.counter.unary_pob_reorg[word].iteritems():
                    t[(i, i, N)] = freq
            else:
                #print word, " mapped to ", rare_label
                for N, freq in self.counter.unary_pob_reorg[rare_label].iteritems():
                    t[(i, i, N)] = freq
            i += 1
        #print t
        
        #calculation
        for l in range(1, n):
            for i in range(1, n - l + 1):
                j = i + l
                for N in self.counter.nonterm.iterkeys(): 
                    if self.counter.binary_pob_reorg.has_key(N):
                        max = 0
                        max_s = i
                        max_Y = None
                        max_Z = None
                        for (Y, Z), freq in self.counter.binary_pob_reorg[N].iteritems():
                            for s in range(i, j):
                                if t.has_key((i, s, Y)) and t.has_key(((s+1, j, Z))):
                                    p = freq * t[(i, s, Y)] * t[(s+1, j, Z)]
                                    #print "none-value", i, j, N, p, s, Y, Z
                                    if p > max:
                                        max = p
                                        max_s = s
                                        max_Y = Y
                                        max_Z = Z
                        if max > 0:
                            t[i, j, N] = max
                            tp[i, j, N] = (max_s, max_Y, max_Z)
                            #print i, j, N, max, (max_s, max_Y, max_Z)
        
        #print t[(1, n, "SBARQ")]
        
        #backpointer for result
        tree = self.constract_result(tp, words, 1, n, "SBARQ")
        print json.dumps(tree)
             

if __name__ == '__main__':
    cky = CKY()
    cky.load_params(sys.argv[1])
    #print cky.counter.unary_pob_reorg[rare_label]
    #print cky.counter.binary_pob_reorg["SBARQ"]
    #print cky.counter.binary_pob_reorg
    #print cky.counter.unary_pob_reorg
    cky.cky(open(sys.argv[2]))