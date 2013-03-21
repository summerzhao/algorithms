'''
Created on Mar 21, 2013

@author: stefaniezhao
'''
import copy
from basic.search.BinarySearchTree import BinarySearchTree
from basic.search.BinarySearchTree import BinaryTreeNode
import matplotlib.pyplot as plt
N = 1
class TwoDTreeNode(BinaryTreeNode):
    HOR = True
    VIL = False
    
    def __init__(self, x, y, direction):
        super(TwoDTreeNode, self).__init__(x, y)
        self.dir = direction

class Object(object):
    pass
       
class Margin(object):
    def __init__(self):
        self.x = Object()
        self.y = Object()
        self.x.max, self.x.min = N, 0
        self.y.max, self.y.min = N, 0
        
    def to_print(self):
        print "x-margin: ", self.x.max, self.x.min, " y-margin: ", self.y.max, self.y.min

class TwoDTree(BinarySearchTree):
    def put(self, x, y):
        self.root = self._put(self.root, x, y, TwoDTreeNode.VIL)
    
    def _put(self, h, x, y, dir):
        if h == None:
            print "create node: ", x, y, dir
            return TwoDTreeNode(x, y, dir)
        if dir == TwoDTreeNode.VIL:
            if x < h.key:
                h.left = self._put(h.left, x, y, not h.dir)
            elif x > h.key:
                h.right = self._put(h.right, x, y, not h.dir)
        else:
            if y < h.value:
                h.left = self._put(h.left, x, y, not h.dir)
            elif y > h.value:
                h.right = self._put(h.right, x, y, not h.dir)    
        h.count = self.size(h.left) + self.size(h.right) + 1
        return h
        
    def visualize(self):
        fig = plt.figure(figsize=(8,4))
        ax = fig.add_axes([0.0, 0.0, 1, 1])
        margin = Margin()
        self._visualize(self.root, margin)
        plt.subplots_adjust()
        plt.show()
    
    def _visualize(self, node, margin):
        if node == None:
            return
        print "node: ", node.key, node.value
        plt.plot([node.key], [node.value], marker='.', color='r', ls='')
        if node.dir == TwoDTreeNode.HOR:
            print "line: ",  margin.x.min, margin.x.max, node.value
            plt.plot([margin.x.min, margin.x.max], [node.value, node.value], color='b')
            #update y min and max
            left_margin = copy.copy(margin)
            left_margin.y.max = node.value
            print "left: ", left_margin.to_print()
            self._visualize(node.left, left_margin)
            
            right_margin = copy.copy(margin)
            right_margin.y.min = node.value
            print "right: ", right_margin.to_print()
            self._visualize(node.right, right_margin)
            
        else:
            print "line: ", node.key, margin.y.min, margin.y.max
            plt.plot([node.key, node.key], [margin.y.min, margin.y.max], color='b')
            #update x min and max
            left_margin = copy.copy(margin)
            left_margin.x.max = node.key
            print "left: ", left_margin.to_print()
            self._visualize(node.left, left_margin)
            
            right_margin = copy.copy(margin)
            right_margin.x.min = node.key
            print "right: ", right_margin.to_print()
            self._visualize(node.right, right_margin)
            
    
def testcase():
    tree = TwoDTree()
    array = [(0.06, 0.69), (0.32, 0.14), (0.44, 0.13), (0.57, 0.23), (0.83, 0.33), (0.67, 0.56), (0.04, 0.03), (0.17, 0.03)] 
    for node in array:
        tree.put(node[0], node[1])
    print tree.level_order_traversal()
    tree.visualize()
           

if __name__ == '__main__':
    testcase()