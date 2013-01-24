'''
Created on 2013-1-24

@author: stefanie
'''
from operator import attrgetter

class Node:
        def __init__(self, name, prob):
            self.name = name
            self.prob = prob
        def setCode(self, code):
            self.code = code
        def __repr__(self):
            return repr((self.name, self.prob))

def huffmanCode(distribution):
    #sorting the distribution
    sorted_distribution = sorted(distribution, key=attrgetter('prob'))
    print sorted_distribution
    

if __name__ == '__main__':
    distribution = [
        Node('a1', 0.1),
        Node('a2', 0.4),
        Node('a3', 0.04),
        Node('a4', 0.1),
        Node('a5', 0.06),
        Node('a6', 0.3),
    ]
    huffmanCode(distribution)
    