'''
Created on Mar 19, 2013

@author: stefaniezhao
'''
import string, random
from basic.search.BinarySearchTree import BinarySearchTree
from basic.search.BinarySearchTree import BinaryTreeNode

class RedBlackTreeNode(BinaryTreeNode):
    RED = True
    BLACK = False
    
    def __init__(self, key, value, color):
        super(RedBlackTreeNode, self).__init__(key, value)
        self.color = color
        

class RedBlackTree(BinarySearchTree):
    '''
    the implementation of left-leaning balance search tree
    '''
    def _rotateLeft(self, h):
        node = h.right
        h.right = node.left
        node.left = h
        node.color = h.color
        h.color = RedBlackTreeNode.RED
        h.count = h.count - 1 - self.size(node.right)
        node.count = node.count + 1 + self.size(h.left)
        return node
    
    def _rotateRight(self, h):
        node = h.left
        h.left = node.right
        node.right = h
        node.color = h.color
        h.color = RedBlackTreeNode.RED
        h.count = h.count - 1 - self.size(node.left)
        node.count = node.count + 1 + self.size(h.right)
        return node
    
    def _flipColors(self, h):
        #assert not self._isRed(h)
        #assert self._isRed(h.left)
        #assert self._isRed(h.right)
        h.color = RedBlackTreeNode.RED
        h.left.color = RedBlackTreeNode.BLACK
        h.right.color = RedBlackTreeNode.BLACK
        
    def _isRed(self, node):
        if node == None:
            return False
        else:
            return node.color == RedBlackTreeNode.RED
        
        
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
    
    def _put(self, h, key, value):
        if h == None:
            return RedBlackTreeNode(key, value, RedBlackTreeNode.RED)
        if key < h.key:
            h.left = self._put(h.left, key, value)
        elif key > h.key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value
            
        h.count = self.size(h.left) + self.size(h.right) + 1
        
        if self._isRed(h.right) and not self._isRed(h.left):
            h = self._rotateLeft(h)
        if self._isRed(h.left) and self._isRed(h.left.left):
            h = self._rotateRight(h)
        if self._isRed(h.left) and self._isRed(h.right):
            self._flipColors(h)
        
        
        return h
            

def testcase4():
    print "testcase4"
    tree = RedBlackTree()
    bi_tree = BinarySearchTree()
    array = random.sample(string.uppercase[:26], 10)
    #array = ['E', 'D', 'L', 'G', 'F', 'H', 'A', 'I', 'B', 'C']
    # array = string.uppercase[:12][::-1]
    print array
    for char in array:
        tree.put(char, char)
        bi_tree.put(char, char)
        print char, tree.level_order_traversal()
        print tree.rank("A")
        
    print tree.level_order_traversal()
    print bi_tree.level_order_traversal()
    
    print tree.inorder_traversal()
        
    #print "search T:", tree.search("T")
    #print "search A:", tree.search("A")
    
    for char in array:
        print char, tree.rank(char), bi_tree.rank(char)
        
    print tree.range_size("A", "G")
    print bi_tree.range_size("D", "G")
    
    print bi_tree.range_node("D", "G")
    
        
if __name__ == '__main__':
    testcase4()     
    