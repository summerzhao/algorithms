'''
Created on Mar 19, 2013

@author: stefaniezhao
'''
from __future__ import division
'''
    Problem: give a set of v_lines and h_lines, find the cross point of these lines.
    Solution:
        1. put all the x-coordination of all the lines in a Priority Queue
        2. scan the queue, create a BinarySearchTree for all the y_coordination,
           if the node is 
            a. the start of a h_line, put it in the tree
            b. the end of a h_line, delete it in the tree
            c. the x_coor of a v_line, find the nodes in the tree in range of the y_coordination of the v_line
        The sweep-line algorithm takes time proportional to NlogN+R to find all R intersections among N orthogonal line segment
        
    Extention to make random case:
        case1: the end point of v_line and h_line are same
            to keep the cross point, scan the h_line first, and if need remove, put the end in an array, 
            remove it after scan all the cross point in the v_line with same y_coordination.
        case2. if the h_line have overlapping:
            put the end of the line in the queue, and check/update the end if have overlapping.
'''


import random
import matplotlib.pyplot as plt
from basic.sortings.ProQueue import QueueNode
from basic.sortings.ProQueue import ProQueue
from basic.search.BinarySearchTree import BinarySearchTree

N = 90
def get_random_int():
    return int(random.uniform(1, N))

def generateLines(N):
    h_lines = []
    v_lines = []
    while len(h_lines) < N:
        y = get_random_int()
        x1 = get_random_int()
        x2 = get_random_int()
        h_lines.append(((x1,y),(x2,y)))
        
        x = get_random_int()
        y1 = get_random_int()
        y2 = get_random_int()
        v_lines.append(((x, y1),(x, y2)))
    return h_lines, v_lines

def build_queue(h_lines, v_lines):
    h_queue = ProQueue()
    for line in h_lines:
        assert(line[0][1] == line[1][1])
        y = line[0][1]
        start = line[0][0]
        end = line[1][0]
        if start < end:
            start, end = end, start 
        #print line, start, end
        h_queue.push(QueueNode(start, (y, end)))
        h_queue.push(QueueNode(end, (y)))
    
    v_queue = ProQueue()
    for line in v_lines:
        #print line
        assert(line[0][0] == line[1][0])
        x = line[0][0]
        if line[1][1] > line[0][1]:
            v_queue.push(QueueNode(x, (line[0][1], line[1][1])))
        else:
            v_queue.push(QueueNode(x, (line[1][1], line[0][1])))
        #print "v_queue", v_queue.get_keys()
    return h_queue, v_queue
    
def find_cross(h_lines, v_lines):
    h_queue, v_queue = build_queue(h_lines, v_lines)
    #print "h_queue", h_queue.get_keys()
    #print "v_queue", v_queue.get_keys()
    tree = BinarySearchTree()
    points = []
    while True:
        v_item = v_queue.pop()
        if v_item != None:
            print "scan", v_item.key
            delete_items = []
            h_item = h_queue.max()
            while h_item != None and h_item.key >= v_item.key:
                h_item = h_queue.pop()
                if type(h_item.value) != type(0): #start node
                    if not tree.contains(h_item.value[0]):
                        print "insert", h_item.value[0], h_item.value[1]
                        tree.put(h_item.value[0], h_item.value[1])
                    else: #overlapping start node
                        end = tree.search(h_item.value[0])
                        print "overlapping start", h_item.value[0]
                        if end > h_item.value[1]:
                            print "update", h_item.value[0], h_item.value[1]
                            tree.put(h_item.value[0], h_item.value[1]) #update the larger end
                        else:
                            print "drop inner section ", h_item.value[1], " within ", end
                else: #end node
                    end = tree.search(h_item.value)
                    assert(end <= h_item.key)
                    if end == h_item.key: #if it's the larger end, remove the y 
                        print "catch the end", end
                        if h_item.key > v_item.key:
                            tree.hibbard_deletion(h_item.value)
                            print "remove", h_item.value, "scan", h_item.key
                        else :
                            delete_items.append(h_item.value)
                h_item = h_queue.max()
            assert v_item.value[1] >= v_item.value[0]
            nodes = tree.range_node(v_item.value[0], v_item.value[1])
            print "find node in range (", v_item.value[0], v_item.value[1], "):", nodes
            for node in nodes:
                points.append((v_item.key, node[0]))
            print "points", points
            print "tree", tree.level_order_traversal()
            print "remove", delete_items
            v_item_next = h_queue.max()
            if v_item_next != None and v_item_next.key < v_item.key: #remove the y when v goes smaller
                for node in delete_items:
                    tree.hibbard_deletion(node)
        else:
            return points
     
def convert(lines):
    converted_lines = []
    for line in lines:
        converted_lines.append(((line[0][0]/N, line[0][1]/N), (line[1][0]/N, line[1][1]/N)))
    return converted_lines


def show_result(h_lines, v_lines, points):
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_axes([0.0, 0.0, 1, 1])
    
    
    #h_lines = convert(h_lines)
    #v_lines = convert(v_lines)
    
    #print h_lines;
    #print v_lines;
    lines = []
    print "h_lines"
    for line in h_lines:
        plt.plot([line[0][0]/N,line[1][0]/N], [line[0][1]/N, line[1][1]/N], color='b')
        
    print "v_lines"   
    for line in v_lines:           
        
        plt.plot([line[0][0]/N,line[1][0]/N], [line[0][1]/N, line[1][1]/N], color='b')
        #lines.append(Line2D(line[0], line[1], transform=fig.transFigure, figure=fig, color="r"))
        
    x_cors = [node[0]/N for node in points]
    print x_cors
    y_cors = [node[1]/N for node in points]
    print y_cors
    #print points
    plt.plot(x_cors, y_cors, marker='.', color='r', ls='')
    
    plt.subplots_adjust()
    #ax.lines.extend(lines)
    plt.show()

def testcase():
    h_lines, v_lines = generateLines(20)
    #h_lines = [((0, 4), (1, 4)), ((2, 5), (5, 5)), ((5, 4), (6, 4)), ((3, 8), (1, 8)), ((3, 7), (8, 7)), ((6, 9), (0, 9)), ((7, 2), (2, 2)), ((6, 7), (6, 7)), ((2, 8), (6, 8)), ((7, 7), (0, 7))]
    #v_lines = [((2, 4), (2, 3)), ((3, 6), (3, 6)), ((6, 6), (6, 8)), ((6, 9), (6, 0)), ((2, 4), (2, 5)), ((1, 8), (1, 8)), ((8, 5), (8, 0)), ((3, 7), (3, 9)), ((3, 1), (3, 9)), ((8, 0), (8, 6))]

    #h_lines = [((9, 6), (2, 6)), ((3, 2), (9, 2)), ((8, 3), (9, 3)), ((6, 7), (9, 7)), ((4, 9), (3, 9)), ((4, 5), (8, 5)), ((9, 4), (4, 4)), ((2, 8), (4, 8)), ((8, 1), (2, 1)), ((1, 1), (4, 1))]
    #v_lines = [((1, 7), (1, 0)), ((1, 2), (1, 6)), ((6, 9), (6, 3)), ((0, 6), (0, 6)), ((7, 3), (7, 0)), ((1, 4), (1, 9)), ((7, 6), (7, 0)), ((5, 1), (5, 1)), ((5, 3), (5, 7)), ((9, 0), (9, 8))]
    print h_lines
    print v_lines
    points = find_cross(h_lines, v_lines)
    print len(points)
    print points
    
    show_result(h_lines, v_lines, points)
    

testcase()
#if __name__ == '__main__':
    