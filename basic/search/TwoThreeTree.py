'''
Created on Mar 18, 2013

@author: stefaniezhao
'''
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import BinaryTreeNode

class TwoNode(BinaryTreeNode):
    '''
    '''
    def __init__(self, key, value):
        super(BinaryTreeNode, self).__init__(key, value)
        self.type = "2"
    
    def change_to_three(self, node):
        self.type = "3"
        if self.right == node:
            self.larger_key = node.key
            self.larger_value = node.value
            self.mid = node.left
            self.right = node.right
        elif self.left == node:
            self.larger_key, self.key = self.key, node.key
            self.mid = node.right
            self.left = node.left
        return self
    
    def change_to_two(self, node):
        if self.mid == node:
            larger_node = BinaryTreeNode(self.larger_key, self.larger_value)
            larger_node.left = node.right
            larger_node.right = self.right
            
            self.right = node.left
            self.type = "2"
            
            node.left = self
            node.right = larger_node
            return node
        elif self.left == node:
            larger_node = BinaryTreeNode(self.larger_key, self.larger_value)
            larger_node.right = self.right
            larger_node.left = self.mid
            
            self.right = larger_node
            self.left = node
            self.type = "2"
            return self
        else:
            larger_node = BinaryTreeNode(self.larger_key, self.larger_value)
            
            self.right = self.mid
            self.type = "2"
            
            larger_node.left = self
            larger_node.right = node
            return larger_node
            
        

class TwoThreeTree(BinarySearchTree):
    '''
    the implementation of two three tree
    '''

    def __init__(self):
        self.root = None
        
        
def testcase4():
    print "testcase4"
        
if __name__ == '__main__':
    testcase4()        