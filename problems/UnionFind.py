'''
Created on 2013-2-17

@author: stefanie

UnionFind is a common problem to find connectivities in a network, problem is:
    have N node, union method could used to connect two nodes in a connectivity, the connection can be transform,
    so if a connected to b, b connected to c, then a is connected to c.
    connected method is used to assert if the two node is connected, A.S. is there a path between the two nodes.

Here give two solution:
    Quick Find, use a int array to store the node, which have a identifier, 
        union is change one of the node identifier to the other through the array. O(N)
        find is check if the identifier of two node is the same or not. O(1)
    Quick Union, use a int array to store the node, the int is the parent node of this node.
        get parent method to loop until the int of the node is same of the identifier, that is the root. O(N)
        union is change one node's parent to the other's parent. O(N)
        find, is check if the parent of the node is same or not. O(N)
    Quick Union could be optimized by balance the tree to avoid tall tree. 2 options:
        1. when do union, check the tree weight.
        2. path compression: during get parent, if the parent is not root, put the grant-parent as parent.
    By optimization, Quick Union could optimize the get parent method to O(lgN)
    
'''
class QuickFind:
    def __init__(self, N): 
        self.num = N
        self.index = []
        for i in range(0, self.num):
            self.index.append(i)
        
    def union(self, a, b):
        flag_a = self.index[a]
        flag_b = self.index[b]
        if flag_a == flag_b:
            return
        for i in range(0, self.num):
            if self.index[i] == flag_a:
                self.index[i] = flag_b
        
    def connected(self, a, b):
        if self.index[a] == self.index[b]:
            return True
        else:
            return False
    
    def toString(self):
        string = " "
        for i in range(0, self.num):
            string += str(self.index[i]) + " "
        return string
    
class QuickUnion:
    def __init__(self, N):
        self.num = N
        self.index = []
        for i in range(0, self.num):
            self.index.append(i)
            
    def getParent(self, a):
        while self.index[a] != a:
            a = self.index[a]
            #add path compression
            self.index[a] = self.index[self.index[a]]
        return a
    
    def union(self, a, b):
        parent_a = self.getParent(a)
        parent_b = self.getParent(b)
        if parent_a != parent_b:
            self.index[parent_a] = parent_b
    
    def connected(self, a, b):
        parent_a = self.getParent(a)
        parent_b = self.getParent(b)
        if parent_a  == parent_b:
            return True
        else:
            return False
        
    def toString(self):
        string = " "
        for i in range(0, self.num):
            string += str(self.index[i]) + " "
        return string
    

def testcase1(finder):
    
    finder.union(4, 3)
    #print finder.toString()
    finder.union(3, 8)
    #print finder.toString()
    finder.union(6, 5)
    #print finder.toString()
    finder.union(9, 4)
    #print finder.toString()
    finder.union(2, 1);
    print finder.connected(0, 7)
    #print finder.find(2)
    print finder.connected(8, 9)
    finder.union(5, 0)
    finder.union(7, 2)
    finder.union(6, 1)
    print finder.toString()
    #print finder.find(2)
    print finder.connected(0, 7)
    
if __name__ == '__main__':
    finder = QuickUnion(10)
    testcase1(finder)
    #testcase2()