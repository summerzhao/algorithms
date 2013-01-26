'''
Created on 2013-1-24

@author: stefanie
'''
from operator import attrgetter

class Node:
        def __init__(self, name, prob):
            self.name = name
            self.prob = prob
            self.code = None
        def setCode(self, code):
            self.code = code
        def __repr__(self):
            if self.code is None:
                return repr((self.name, self.prob))
            else:
                return repr((self.name, self.prob, self.code))
        
class TreeNode:
        def __init__(self, prob, left, right):
            self.prob = prob
            self.left = left
            self.right = right
            
        def setLeft(self, node):
            self.left = node
            
        def setRight(self, node):
            self.right = node
            
        def __repr__(self):
            return repr(self.prob)
            
def assignCode(node, prefix):
        #print node
        if isinstance(node, TreeNode):
            assignCode(node.left, prefix+'0')
            assignCode(node.right, prefix+'1')
        else:
            node.code = prefix
            #print node

def huffmanCode(distribution):
    if len(distribution) > 1:
        #sorting the distribution
        sorted_distribution = sorted(distribution, key=attrgetter('prob'))
        #print sorted_distribution
        while len(sorted_distribution) > 2:
            node1 = sorted_distribution.pop(0)
            node2 = sorted_distribution.pop(0);
            #contruct a new tree node for the most small prob node
            newNode = TreeNode(node1.prob + node2.prob, node1, node2)
            #insert the treeNode into the sorted_distribution
            added = False
            for index in range(0, len(sorted_distribution)):
                if newNode.prob < sorted_distribution[index].prob:
                    sorted_distribution.insert(index, newNode)
                    added = True
                    break;
            if not added:
                sorted_distribution.append(newNode)
            #print sorted_distribution
    else :
        i = 0
        for node in distribution:
            node.setCode(i)
            i+=1
            
    #assign code
    assignCode(sorted_distribution[0], '0')
    assignCode(sorted_distribution[1], '1')

def build_encode_map(distribution):
    dict = {}
    for node in distribution:
        dict[node.name] = node.code
    return dict

def build_decode_map(distribution):
    dict = {}
    for node in distribution:
        dict[node.code] = node.name
    return dict

def encode(str, encode_map):
    encodeStr = ""
    for ch in str:
        if ch in encode_map.keys():
            encodeStr += encode_map[ch]
        else:
            print "input contains invalid char"
            return None
    return encodeStr

def decode(str, decode_map):
    decodeStr = ""
    currentStr = ""
    for ch in str:
        currentStr += ch
        if currentStr in decode_map.keys():
            decodeStr+= decode_map[currentStr]
            currentStr = ""
    if len(currentStr) > 0:
        print "can't decode input, contains invalid match"
        return None
    else :
        return decodeStr

def test_encode_decode(test_str, distribution):
    encode_map = build_encode_map(distribution)
    encode_str = encode(test_str, encode_map)
    print "Encode ", test_str, " is ", encode_str
    
    decode_map = build_decode_map(distribution)
    decode_str = decode(encode_str, decode_map)
    print "Decode ", encode_str, " is ", decode_str  
    
def testcase1():
    print "--------Test Case 1 ---------------"
    distribution = [
        Node('a', 0.1),
        Node('b', 0.4),
        Node('c', 0.04),
        Node('d', 0.1),
        Node('e', 0.06),
        Node('f', 0.3),
    ]
    print distribution
    huffmanCode(distribution)
    print distribution
    
    test_str = "afdcbbce"
    test_encode_decode(test_str, distribution)
    
    
#    sorted_distribution = sorted(distribution, key=attrgetter('prob'))
#    print sorted_distribution
    print 

def testcase2():
    print "--------Test Case 2 ---------------"    
    distribution = [
        Node('g', 3),
        Node('o', 3),
        Node('_', 2),
        Node('e', 1),
        Node('s', 1),
        Node('h', 1),
        Node('p', 1),
        Node('r', 1),
    ]
    print distribution
    huffmanCode(distribution)
    print distribution
    
    test_str = "ego_hesspher"
    test_encode_decode(test_str, distribution)
    
#    sorted_distribution = sorted(distribution, key=attrgetter('prob'))
#    print sorted_distribution
    print 

if __name__ == '__main__':
    testcase1()
    testcase2()
    