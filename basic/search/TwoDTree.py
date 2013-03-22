'''
Created on Mar 21, 2013

@author: stefaniezhao
'''

'''
    Problem: 
        1. Range search in 2D points
        2. Find nearest point in 2D
    Solution:
        2D tree is designed to use Tree to represent a recursive subdivision of 2d space.
        2D tree is a BST alternate using x-coordinate and y-coordinate as key
        
        For 1:
            a. check if point in node lines in a given rectangle
            b. recursively search left/bottom if any could fall in
            c. recursively search right/top if any could fall in
            Typical R+lgN, Worst: R+N^1/2
            
        For 2:
            a. check distance from point in node to query point
            b. recursively search left/bottom if it could contain a closer point
            c. recursively search right/top if it could contain a closer point
            d. orginaze method so that it begins by searching for query point
            Typical: logN, worst: N
'''

import random
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
        
    def clone(self):
        clone = Margin()
        clone.x.max, clone.x.min = self.x.max, self.x.min
        clone.y.max, clone.y.min = self.y.max, self.y.min
        return clone

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
            plt.plot([margin.x.min, margin.x.max], [node.value, node.value], color='y')
            #update y min and max
            left_margin = margin.clone()
            left_margin.y.max = node.value
            print "left: ", left_margin.to_print()
            self._visualize(node.left, left_margin)
            
            right_margin = margin.clone()
            right_margin.y.min = node.value
            print "right: ", right_margin.to_print()
            self._visualize(node.right, right_margin)
            
        else:
            print "line: ", node.key, margin.y.min, margin.y.max
            plt.plot([node.key, node.key], [margin.y.min, margin.y.max], color='b')
            #update x min and max
            left_margin = margin.clone()
            left_margin.x.max = node.key
            print "left: ", left_margin.to_print()
            self._visualize(node.left, left_margin)
            
            right_margin = margin.clone()
            right_margin.x.min = node.key
            print "right: ", right_margin.to_print()
            self._visualize(node.right, right_margin)
            
def generatePoints():   
    array = []
    for i in range(0, 20):
        x = random.uniform(0, N)
        y = random.uniform(0, N)
        array.append((x, y))
    return array
    
def testcase():
    tree = TwoDTree()
    #array = generatePoints()
    #array = [(0.06, 0.69), (0.32, 0.14), (0.44, 0.13), (0.57, 0.23), (0.83, 0.33), (0.67, 0.56), (0.04, 0.03), (0.17, 0.03)] 
    #array = [(0.18,0.54),(0.8,0.05),(0.2,0.06),(0.24,0.15),(0.32,0.77),(0.5,0.89),(0.93,0.51),(0.86,0.94)]
    array = [(0.75,0.16),(0.9,0.8),(0.02,0.35),(0.51,0.77),(0.15,0.41),(0.08,0.65),(0.78,0.30),(0.89,0.63)]
    for node in array:
        tree.put(node[0], node[1])
    print tree.level_order_traversal()
    tree.visualize()
           

if __name__ == '__main__':
    testcase()