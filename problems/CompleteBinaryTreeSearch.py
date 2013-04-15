'''
Created on Apr 15, 2013

@author: stefaniezhao
'''
from collections import deque #used in generate sample tree

class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.next = None
        
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
        

class Tree(object):
    def __init__(self, root):
        self.root = root
        
def search(tree):
    #init parent is the root of the tree
    parent = tree.root
    #init parent's next is the left child of the root
    parent.next = parent.left
    #current is the next searching node
    current = parent.left
    #index variables is the index of current in the searching process
    index = 2
    while(current != None):
        # the rule is reduced based on complete binary tree
        if index % 2 == 0: #even number, it should be the left child of its parent, 
                            #its next is the right child of the parent
            current.next = parent.right
        else: # odd number, it should be the right child of its parent, 
                # its next should be the left child of the next of its parent
            parent = parent.next
            current.next = parent.left
        current = current.next
        index += 1
    return tree
        
def sample(n):
    #build a sample complete binary tree
    root = Node(1, None, None)
    tree = Tree(root)

    queue = deque()       
    queue.append(tree.root)
    for i in range(2, n+1)[::2]:
        parent = queue.popleft() 
        left = Node(i, None, None)
        right = Node(i + 1, None, None)
        parent.left = left
        parent.right = right
        queue.append(left)
        queue.append(right)
        
    return tree

#test method
if __name__ == '__main__':
    tree = sample(11)
    enhance_tree = search(tree)
    node = tree.root
    while node != None:
        print node.value
        node = node.next
    
        
        