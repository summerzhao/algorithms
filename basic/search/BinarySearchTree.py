'''
Created on 2013-3-17

@author: stefanie
'''

from collections import deque
class BinaryTreeNode(object):
    '''
        the node of binary tree
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = 1
        
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
        
    
class BinarySearchTree(object):
    '''
    the implementation of binary search tree
    '''

    def __init__(self):
        self.root = None
        
    def _put(self, node, key, value):
        if node == None:
            return BinaryTreeNode(key, value)
        else:
            if node.key > key:
                node.left = self._put(node.left, key, value)
            elif node.key < key:
                node.right = self._put(node.right, key, value)
            else:
                node.value = value
        node.count = self.size(node.left) + self.size(node.right) + 1
        return node
        
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        
    def _search(self, node, key):
        if node == None:
            return None
        if node.key == key:
            return node.value
        elif node.key > key:
            return self._search(node.left, key)
        elif node.key < key:
            return self._search(node.right, key)
        else:
            return None
        
    def search(self, key):
        return self._search(self.root, key)
    
    def contains(self, key):
        return self.search(key) != None
    
    def max(self):
        node = self.root
        while node.right != None:
            node = node.right
        return node.value
        
    def min(self):
        node = self.root
        while node.left != None:
            node = node.left
        return node.value
    
    def _min(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def floor(self, k):
        floor = self._floor(self.root, k)
        if floor == None: 
            return None
        else:
            return floor.value
        
    def _floor(self, node, k):
        if node == None:
            return None
        if node.key == k:
            return node
        elif node.key > k:
            return self._floor(node.left, k)
        else:
            # if node need floor element in the right subtree, need return the parent of the subtree
            floor = self._floor(node.right, k);
            if floor == None:
                return node
            else:
                return floor
            
    def ceil(self, k):
        ceil = self._ceil(self.root, k)
        if ceil == None:
            return None
        else:
            return ceil.value
    
    def _ceil(self, node, k):
        if node == None:
            return None
        if node.key == k:
            return node
        elif node.key < k:
            return self._ceil(node.right, k)
        else:
            ceil = self._ceil(node.left, k)
            if ceil == None:
                return node
            else:
                return ceil
            
    def height(self):
        return self._height(self.root)
        
    def _height(self, node):
        if node == None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1
        
    def size(self, node):
        if node != None:
            return node.count
        else:
            return 0
        
    def rank(self, k):
        return self._rank(self.root, k)
        
    def _rank(self, node, k):
        if node == None:
            return 0
        if node.key == k:
            return self.size(node.left)
        elif node.key > k:
            return self._rank(node.left, k)
        else:
            return 1 + self.size(node.left) + self._rank(node.right, k)
        
    def _delete_min(self, node):
        if node.left == None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = self.size(node.left) + self.size(node.right) + 1
        return node
    
    def hibbard_deletion(self, k):
        self.root = self._hibbard_deletion(self.root, k)
    
    def _hibbard_deletion(self, node, k):
        if node == None:
            return None
        if node.key > k:
            node.left = self._hibbard_deletion(node.left, k)
        elif node.key < k:
            node.right = self._hibbard_deletion(node.right, k)
        else:
            if node.right == None:
                return node.left
            else:
                t = node;
                node = self._min(t.right)
                node.right = self._delete_min(t.right)
                node.left = t.left
        node.count = self.size(node.left) + self.size(node.right) + 1
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
            array.append(item.value)
            if item.left != None:
                queue.append(item.left)
            if item.right != None:
                queue.append(item.right) 
        return array           
    
    def inorder_traversal(self):  # depth-first searching
        array = []
        self._inorder_traversal(self.root, array)
        return array
        
    def _inorder_traversal(self, node, array): 
        if node == None: 
            return
        self._inorder_traversal(node.left, array)
        array.append(node.value)
        self._inorder_traversal(node.right, array)
        
    def range_size(self, low, high):
        if self.contains(high):
            return self.rank(high) - self.rank(low) + 1
        else:
            return self.rank(high) - self.rank(low)
        
    def range_node(self, low, high):
        return self._range_node(self.root, low, high)
        
    def _range_node(self, node, low, high):
        array = []
        if node != None:
            if node.key >= low and node.key <= high:
                array.append(node.value)
                if node.key > low:
                    array += self._range_node(node.left, low, high)
                if node.key < high:
                    array += self._range_node(node.right, low, high)
            elif node.key < low:
                array += self._range_node(node.right, low, high)
            else:
                array += self._range_node(node.left, low, high)
        return array
        
            
    
def testcase1():
    BST = BinarySearchTree()
    # array = [91, 34, 18, 69, 59, 88, 58, 65, 38, 46]
    array = [33, 10, 63, 25, 45, 95, 12, 54, 64, 57, 80, 74]
    for node in array:
        BST.put(node, node)
        
    print BST.level_order_traversal()
    BST.hibbard_deletion(57)
    print "57:", BST.level_order_traversal()
    BST.hibbard_deletion(64)
    print "64:", BST.level_order_traversal()
    BST.hibbard_deletion(63)
    print "63:", BST.level_order_traversal()
    print BST.inorder_traversal()
    print BST.search(60)
    
    print BST.max()
    print BST.min()
    print BST.floor(77)
    print BST.ceil(57)
    print BST.height()
    print BST.rank(57)
    
def testcase2():
    BST = BinarySearchTree()
    BST.put(65, 65)
    BST.put(87, 87)
    
    print BST.level_order_traversal()
    
    BST.hibbard_deletion(65)
    print BST.level_order_traversal()
    
        
if __name__ == '__main__':
    testcase2()  
