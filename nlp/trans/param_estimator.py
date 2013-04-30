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
    for en in corpus_en: #iterative on sample sent pair 
        es = corpus_es.readline().strip()       
        en_w = en.strip().split(" ")
        es_w = set(es.split(" "))
        #print en_w
        #print es_w
        for w in en_w:
            if w not in d:
                d[w] = set()
            d[w] = d[w].union(es_w)
        d['NULL'] = d['NULL'].union(es_w)
    #print d
    #print d
    #print len(d)
    for w in d:
        d[w] = len(d[w])
    #print d
    return d
        

def main(t_map, corpus_en, corpus_es):
    #print "enter_main"
    q_map=defaultdict(float)

    for s in range(1, iteration + 1): #iterative on iteration
        #print "Iterater", s
        #print s
        #print t_map
        c = defaultdict(float)
        ce= defaultdict(float)
        ci = defaultdict(float)
        cij= defaultdict(float)
        k = 1
        for en in corpus_en:
            
            es = corpus_es.readline().strip()        
            en_w = en.strip().split(" ")
            es_w = es.split(" ")
            
            m = len(es_w)
            l = len(en_w)
            #q = 1/(l+1)
            for i in range(1, m+1): 
                r = defaultdict(float)        
                total = 0
                f = es_w[i-1]
                for j in range(0, l+1):
                    e = None
                    if j == 0:
                        e = 'NULL'
                    else:
                        e = en_w[j-1]
                    t = t_map[e][f]
                    if s == 1:
                        #print e, d[e]
                        q = 1/(l+1)
                    else:
                        #print e, f
                        #print t_map                        
                        q = q_map[(i,j,m,l)]
                    #print t
                    r[j] = t * q 
                    total += r[j]
                    #print total
                    #print s
                #print "total",  total
                for j in range(0, l+1):
                    r[j] = r[j]/total
                    e = None
                    if j == 0:
                        e = 'NULL'
                    else:
                        e = en_w[j-1]
                    f = es_w[i-1]
                    if (e,f) in c:
                        c[(e,f)] += r[j]
                    else:
                        c[(e,f)] = r[j]
                    if e in ce:
                        ce[e] += r[j]
                    else:
                        ce[e] = r[j]
                    cij[(i,j,m,l)] += r[j]
                    ci[(i,m,l)] += r[j]
                #print len(c), len(ce), len(cij), len(ci)
                #print cij
            k+= 1
        t_map = {}
        q_map=defaultdict(float)
        #print c
        for (e, f), count in c.items():
            if e not in t_map:
                t_map[e] = defaultdict(float)
            t_map[e][f] = count/ce[e]
        
        
        for (i,j,m,l), count in cij.items():
            q_map[(i,j,m,l)] = count/ci[(i,m,l)]
            
        corpus_en.seek(0,0)
        corpus_es.seek(0,0)
    return t_map, q_map   

def print_t(t,q):
    for e, map in t.items():
        for f, count in map.items():
            print "MLT", e, f, count   
            
    for (i,j,m,l), count in q.items():
        print "MLQ", i, j, m, l, count
    
def allignment(t,q, data_en, data_es):    
    k = 1
    for en in data_en: #iterative on sample sent pair
        es = data_es.readline().strip() 
        en_w = en.strip().split(" ")
        es_w = es.split(" ")
            
        m = len(es_w)
        l = len(en_w) 
        allign = []
        
        i = 0
        for f in es_w:
            i += 1
            max = 0
            if f in t['NULL']:
                max = t['NULL'][f]*q[(i,0,m,l)]
                #print i, m, l, q[(i,0,m,l)]
                #print max
            max_j = 0
            for j in range(1, l+1):
                e = en_w[j-1]
                if e in t and f in t[e]:
                    #print i, j, m, l, q[(i,j,m,l)]
                    s = t[e][f]*q[(i,j,m,l)]
                    if s > max:
                        max = s
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
        k+= 1
  
def load_t(count): 
    t = {}
    for line in count:
        units = line.split(" ");
        if units[0] not in t:
            t[units[0]] = {}
        t[units[0]][units[1]] = float(units[2])
    return t
    
def load_parameter(count):
    t = {}
    q = defaultdict(float)
    for line in count:
        units = line.split(" ");
        if units[0] == "MLT":
            if units[1] not in t:
                t[units[1]] = {}
            t[units[1]][units[2]] = float(units[3])
        elif units[0] == "MLQ":
            #print line
            #print "MLQ", i, j, m, l, count
            #print len(units)
            q[(int(units[1]),int(units[2]),int(units[3]),int(units[4]))] = float(units[5])
            #print q
    #print t
    #MLQ 36 9 40 45 0.0083692758436
    #MLQ 25 36 37 41 0.0129615947169
    #MLQ 36 35 40 44 0.0381103138154
    #MLQ 66 5 118 76 5.7793465647e-10
    #MLQ 35 1 37 35 0.00287731679006
    #MLQ 9 28 65 61 0.0240896006149
    #print q[(66, 5, 118, 76)];
    #print q[(35, 1, 37, 35)];
    #print q[(9, 28, 65, 61)];
    return t,q
            
    
def allignment_main():
    count = file(sys.argv[1], "r")
    t, q = load_parameter(count)
    #print t['all']
    #print len(t['all'])
    data_en = file(sys.argv[2], "r")
    data_es = file(sys.argv[3], "r")
    allignment(t, q, data_en, data_es)
    
def print_init(d):
    for w, count in d.items():
        print w, count
        
def load_init(d_file):
    d = {}
    for line in d_file:
        #print line
        units = line.split(" ");
        d[units[0]] = int(units[1])
    return d
        
    
def estimate():
    t_file = file(sys.argv[1], "r")
    corpus_en = file(sys.argv[2], "r")
    corpus_es = file(sys.argv[3], "r")
    
    #d = init(corpus_en, corpus_es)
    #d = load_init(d_file)
    t= load_t(t_file)
    #print "after load"
    
    #corpus_en.seek(0,0)
    #corpus_es.seek(0,0)
    t,q = main(t, corpus_en, corpus_es)
    
    print_t(t,q)
    #return t

if __name__ == "__main__": 
    #t = estimate()
    #print t['all']
    #print len(t['all'])
    allignment_main()
    
    
    
    