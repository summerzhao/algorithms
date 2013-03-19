'''
Created on Mar 18, 2013

@author: stefaniezhao
'''
import string, random
from basic.search.BinarySearchTree import BinarySearchTree
from basic.search.BinarySearchTree import BinaryTreeNode
from collections import deque

class TwoThreeTreeNode(BinaryTreeNode):
    '''
    '''
    def __init__(self, key, value):
        super(TwoThreeTreeNode, self).__init__(key, value)
        # super().__init__(key, value)
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
            self.larger_value, self.value = self.value, node.value
            self.mid = node.right
            self.left = node.left
        return self
    
    def change_to_two(self, node):
        if self.mid == node:
            larger_node = TwoThreeTreeNode(self.larger_key, self.larger_value)
            larger_node.left = node.right
            larger_node.right = self.right
            
            self.right = node.left
            self.type = "2"
            
            node.left = self
            node.right = larger_node
            return node
        elif self.left == node:
            larger_node = TwoThreeTreeNode(self.larger_key, self.larger_value)
            larger_node.right = self.right
            larger_node.left = self.mid
            
            self.right = larger_node
            self.left = node
            self.type = "2"
            return self
        else:
            larger_node = TwoThreeTreeNode(self.larger_key, self.larger_value)
            
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
    
    def search(self, key):
        node = self.root
        while node != None:
            if node.type == "2":
                if key > node.key:
                    node = node.right
                    continue
                elif key < node.key:
                    node = node.left
                    continue
                else:
                    return node.value
            else:
                if key == node.larger_key:
                    return node.larger_value
                elif key == node.key:
                    return node.value
                elif key < node.key:
                    node = node.left
                    continue
                elif key > node.larger_key:
                    node = node.right
                    continue
                else:
                    node = node.mid
                    continue
        return None
                
        
    def put(self, value, key):
        self.root = self._put(self.root, key, value)
        
    def _put(self, node, key, value):
        if node == None:
            return TwoThreeTreeNode(key, value)
        elif node.type == "2":
            if node.key > key:
                node.left = self._put(node.left, key, value)
                if node.left.type == "2":
                    return node.change_to_three(node.left)
                else:
                    return node
            elif node.key < key:
                node.right = self._put(node.right, key, value)
                if node.right.type == "2":
                    return node.change_to_three(node.right)
                else:
                    return node
            else:
                node.value = value
                return node
        elif node.type == "3":
            if node.key == key:
                node.value = value
                return node
            elif node.larger_key == key:
                node.larger_value = value
                return node
            elif node.key > key:
                node.left = self._put(node.left, key, value)
                if node.left.type == "2":
                    return node.change_to_two(node.left)
                else:
                    return node
            elif node.larger_key < key:
                node.right = self._put(node.right, key, value)
                if node.right.type == "2":
                    return node.change_to_two(node.right)
                else:
                    return node
            else:
                node.mid = self._put(node.mid, key, value)
                if node.mid.type == "2":
                    return node.change_to_two(node.mid)
                else:
                    return node
                
    def level_order_traversal(self):  # breadth-first searching
        array = []
        queue = deque([])
        queue.append(self.root)
        queue.append("|")
        while(len(queue) > 0):
            item = queue.popleft();
            if item == "|":
                array.append("|");
                if len(queue) > 0:
                    queue.append("|")
                continue
            if item.type == "2":
                array.append(item.value)
            else:
                array.append("(" + item.value + "," + item.larger_value + ")")
            if item.left != None:
                queue.append(item.left)
            if item.type == "3" and item.mid != None:
                queue.append(item.mid)
            if item.right != None:
                queue.append(item.right) 
        return array          
        
        
def testcase4():
    print "testcase4"
    tree = TwoThreeTree()
    array = random.sample(string.uppercase[:12], 10)
    # array = string.uppercase[:12][::-1]
    print array
    for char in array:
        tree.put(char, char)
        print tree.level_order_traversal()
        
    print tree.search("T")
    print tree.search("A")
        
if __name__ == '__main__':
    testcase4()        
