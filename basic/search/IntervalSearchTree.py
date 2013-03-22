'''
Created on 2013-3-21

@author: stefanie
'''

'''
    Problem: give a set of intervals, and find a interval intersects in the given search interval.
    
    Solution:
        Build a interval search tree based on BST, using min as the key, and keep the max endpoint in subtree rooted at the end
        
        For Insert:
            1. insert interval in BST
            2. update the max in each node on search path
            
        For Search:
            a. if the interval in node intersects query interval, return interval
            b. else if left subtree is null or the max endpoint in left subtree is less than lo, go right.
            c. else go left
'''

import random
from basic.search.BinarySearchTree import BinarySearchTree
from basic.search.BinarySearchTree import BinaryTreeNode
N = 100
class IntervalSearchTreeNode(BinaryTreeNode):
    def __init__(self, lo, hi):
        super(IntervalSearchTreeNode, self).__init__(lo, hi)
        self.max = hi
    
    def to_print(self):
        return (self.key, self.value)

class IntervalSearchTree(BinarySearchTree):
    def put(self, lo, hi):
        self.root = self._put(self.root, lo, hi)
    
    def _put(self, node, lo, hi):
        if node == None:
            return IntervalSearchTreeNode(lo, hi)
        else:
            if node.key > lo:
                node.left = self._put(node.left, lo, hi)
                if node.left.value > node.max:
                    node.max = node.left.value
            elif node.key < hi:
                node.right = self._put(node.right, lo, hi)
                if node.right.value > node.max:
                    node.max = node.right.value
        node.count = self.size(node.left) + self.size(node.right) + 1
        return node
    
    def search(self, lo, hi):
        #return self._search(lo, hi, self.root)
        node = self.root
        while node != None:
            print node.key, node.value
            if lo > node.key and hi < node.value:
                return node.to_print()
            elif node.left == None or node.left.max < lo:
                #print node.key, lo
                if node.key > lo:
                    return None
                else:
                    node = node.right
            else:
                node = node.left
        return None
    
    def _search(self, lo, hi, node):
        if node == None:
            return None
        elif lo > node.key and hi < node.value:
            return node.to_print()
        elif node.left == None or node.left.max < lo:
            return self._search(lo, hi, node.right)
        else:
            return self._search(lo, hi, node.left)
        
def testcase():
    num = 20
    intervals = []
    tree = IntervalSearchTree()
    for i in range(0, num):
        min = int(random.uniform(1, N))
        max = int(random.uniform(1, N))
        
        if min > max:
            min, max = max, min
        
        if i < num-5:
            tree.put(min, max)
        else:
            intervals.append((min, max))
            
    print tree.level_order_traversal()
    for interval in intervals:
        print "search: ", interval, " found: ", tree.search(interval[0], interval[1])

def testcase1():
    intervals = [(16,20),(34,39),(28,35),(31,40),(32,37),(13,17),(6,21),(2,22)]
    tree = IntervalSearchTree()
    for interval in intervals:
        tree.put(interval[0], interval[1])
    print tree.level_order_traversal()
    print tree.search(25,27)
       
if __name__ == '__main__':
    testcase1()      
            
    
        
    
        
    