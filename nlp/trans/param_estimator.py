from __future__ import division
'''
Created on 2013-4-25

@author: stefanie
'''
import sys, math
from collections import defaultdict

iteration = 5

def init(corpus_en, corpus_es):
    d = {}
    d['NULL'] = set()
    en = corpus_en.readline().strip()
    while en: #iterative on sample sent pair
        es = corpus_es.readline().strip()          
        en_w = en.split(" ")
        es_w = set(es.split(" "))
        #print en_w
        #print es_w
        for w in en_w:
            if w in d:
                d[w] = d[w].union(es_w)
            else:
                d[w] = es_w
        d['NULL'] = d['NULL'].union(es_w)
        en = corpus_en.readline().strip()
    #print d
    
    for w in d:
        d[w] = len(d[w])
    #print d
    return d
        

def main(d, corpus_en, corpus_es):
    r = defaultdict(float)
    t_map = {}
    for s in range(1, iteration + 1): #iterative on iteration
        #print s
        #print t_map
        c = defaultdict(float)
        ce= defaultdict(float)
        k = 1
        en = corpus_en.readline().strip()
        while en: #iterative on sample sent pair
            es = corpus_es.readline().strip()           
            en_w = en.split(" ")
            es_w = es.split(" ")
            
            m = len(es_w)
            l = len(en_w)
            #q = 1/(l+1)
            
            for i in range(1, m+1):
                sum = 0
                for j in range(0, l+1):
                    e = None
                    if j == 0:
                        e = 'NULL'
                    else:
                        e = en_w[j-1]
                    f = es_w[i-1]
                    t = None
                    if s == 1:
                        t = 1/d[e]
                    else:
                        #print e, f
                        #print t_map
                        t = t_map[e][f]
                    #print t
                    r[(k,i,j)] = t 
                    sum += r[(k,i,j)]
                for j in range(0, l+1):
                    r[(k,i,j)] = r[(k,i,j)]/sum
                    e = None
                    if j == 0:
                        e = 'NULL'
                    else:
                        e = en_w[j-1]
                    f = es_w[i-1]
                    if (e,f) in c:
                        c[(e,f)] += r[(k,i,j)]
                    else:
                        c[(e,f)] = r[(k,i,j)]
                    if e in ce:
                        ce[e] += r[(k,i,j)]
                    else:
                        ce[e] = r[(k,i,j)]
            en = corpus_en.readline().strip()
            k+= 1
        t_map = {}
        #print c
        for (e, f), count in c.iteritems():
            if e not in t_map:
                t_map[e] = {}
            t_map[e][f] = count/ce[e]
        corpus_en.seek(0,0)
        corpus_es.seek(0,0)
#        print "-----------Interation " + str(s) + "--------------"
#        print_t(t_map)
    return t_map    

def print_t(t):
    for e, map in t.iteritems():
        for f, count in map.iteritems():
            print e, f, count   
    
def allignment(t, data_en, data_es):    
    en = data_en.readline().strip()
    k = 1
    while en: #iterative on sample sent pair
        es = data_es.readline().strip() 
        en_w = en.split(" ")
        es_w = es.split(" ")
            
        m = len(es_w)
        l = len(en_w) 
        allign = []
        
        for f in es_w:
            max = 0
            if f in t['NULL']:
                max = t['NULL'][f]
            max_j = 0
            for j in range(1, l+1):
                e = en_w[j-1]
                if e in t and f in t[e]:
                    if t[e][f] > max:
                        max = t[e][f]
                        max_j = j
            allign.append(max_j)

#        for e in en_w:
#            max = 0;
#            max_i = 0
#            for i in range(1, m+1):
#                f = es_w[i-1]
#                if e in t and f in t[e]:
#                    if t[e][f] > max:
#                        max = t[e][f]
#                        max_i = i
#            allign.append(max_i)
        
#        i = 1
#        for a in allign:
#            if a != 0:
#                print k, i, a
#            i += 1
        
        i = 1
        for a in allign:
            if a != 0:
                print k, a, i
            i += 1
        en = data_en.readline().strip()
        k+= 1
    
def allignment_main(t):
    data_en = file(sys.argv[3], "r")
    data_es = file(sys.argv[4], "r")
    allignment(t, data_en, data_es)
    
    
if __name__ == "__main__": 
    corpus_en = file(sys.argv[1], "r")
    corpus_es = file(sys.argv[2], "r")
    
    d = init(corpus_en, corpus_es)
    corpus_en.seek(0,0)
    corpus_es.seek(0,0)
    t = main(d, corpus_en, corpus_es)
    allignment_main(t)
    
    
    #print_t(t)
    