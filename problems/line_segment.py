'''
Created on Mar 19, 2013

@author: stefaniezhao
'''
from __future__ import division
import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from basic.sortings.ProQueue import QueueNode
from basic.sortings.ProQueue import ProQueue
from basic.search.BinarySearchTree import BinarySearchTree

def get_random_int():
    return int(random.uniform(0, 50))

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
            #print "scan", v_item.key
            delete_items = []
            h_item = h_queue.max()
            while h_item != None and h_item.key >= v_item.key:
                h_item = h_queue.pop()
                if type(h_item.value) != type(0): #start node
                    if not tree.contains(h_item.value[0]):
                        #print "insert", h_item.value[0], h_item.value[1]
                        tree.put(h_item.value[0], h_item.value[1])
                    else: #overlapping start node
                        end = tree.search(h_item.value[0])
                        #print "overlapping start", h_item.value[0]
                        if end > h_item.value[1]:
                            #print "update", h_item.value[0], h_item.value[1]
                            tree.put(h_item.value[0], h_item.value[1]) #update the larger end
                        #else:
                            #print "drop inner section ", h_item.value[1], " within ", end
                else: #end node
                    end = tree.search(h_item.value)
                    assert(end <= h_item.key)
                    if end == h_item.key: #if it's the larger end, remove the y 
                        #print "catch the end", end
                        if h_item.key > v_item.key:
                            tree.hibbard_deletion(h_item.value)
                            #print "remove", h_item.value, "scan", h_item.key
                        else :
                            delete_items.append(h_item.value)
                h_item = h_queue.max()
            assert v_item.value[1] >= v_item.value[0]
            nodes = tree.range_node(v_item.value[0], v_item.value[1])
            #print "find node in range (", v_item.value[0], v_item.value[1], "):", nodes
            for node in nodes:
                points.append((v_item.key, node[0]))
            #print "points", points
            #print "tree", tree.level_order_traversal()
            #print "remove", delete_items
            v_item_next = h_queue.max()
            if v_item_next != None and v_item_next.key < v_item.key: #remove the y when v goes smaller
                for node in delete_items:
                    tree.hibbard_deletion(node)
        else:
            return points
N = 50      
def convert(lines):
    converted_lines = []
    for line in lines:
        converted_lines.append(((line[0][0]/N, line[0][1]/N), (line[1][0]/N, line[1][1]/N)))
    return converted_lines


def show_result(h_lines, v_lines, points):
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_axes([0.0, 0.0, 1, 1])
    points = [[node[0]/N, node[1]/N] for node in points]
    print points
    plt.plot(*zip(*points), marker='o', color='r', ls='')
    
    #h_lines = convert(h_lines)
    #v_lines = convert(v_lines)
    
    #print h_lines;
    #print v_lines;
    
    lines = []
    for line in h_lines:
        #lines.append(Line2D(line[0], line[1], transform=fig.transFigure, figure=fig, color="r"))
        y_cor = line[0][1]/N
        start = line[0][0]/N
        end = line[1][0]/N
        if start < end:
            start, end = end, start             
        plt.axhline(y=y_cor, xmin=end, xmax=start, color='b')
        
        
    for line in v_lines:
        x_cor = line[0][0]/N
        print x_cor
        start = line[0][1]/N
        end = line[1][1]/N
        if start < end:
            start, end = end, start
        print x_cor, end, start             
        plt.axvline(x=x_cor, ymin=end, ymax=start, color='b')
        #lines.append(Line2D(line[0], line[1], transform=fig.transFigure, figure=fig, color="r"))
        
    
        
    #ax.lines.extend(lines)
    plt.show()

def testcase():
    h_lines, v_lines = generateLines(10)
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
    