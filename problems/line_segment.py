'''
Created on Mar 19, 2013

@author: stefaniezhao
'''
import random
from basic.sortings.ProQueue import QueueNode
from basic.sortings.ProQueue import ProQueue
from basic.search.BinarySearchTree import BinarySearchTree

def get_random_int():
    return int(random.uniform(0, 10))

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
        h_queue.push(QueueNode(line[0][0], (y)))
        h_queue.push(QueueNode(line[1][0], (y)))
    
    v_queue = ProQueue()
    for line in v_lines:
        assert(line[0][0] == line[1][0])
        x = line[0][0]
        if line[1][1] > line[0][1]:
            v_queue.push(QueueNode(x, (line[0][1], line[1][1])))
        else:
            v_queue.push(QueueNode(x, (line[1][1], line[0][1])))
    return h_queue, v_queue
    
def find_cross(h_lines, v_lines):
    h_queue, v_queue = build_queue(h_lines, v_lines)
    tree = BinarySearchTree()
    points = []
    while True:
        v_item = v_queue.pop()
        if v_item != None:
            h_item = h_queue.max()
            while h_item != None and h_item.key >= v_item.key:
                h_item = h_queue.pop()
                if not tree.contains(h_item.value):
                    tree.put(h_item.value, h_item.value)
                else:
                    tree.hibbard_deletion(h_item.value)
                h_item = h_queue.max()
            assert v_item.value[1] >= v_item.value[0]
            nodes = tree.range_node(v_item.value[0], v_item.value[1])
            for node in nodes:
                points.append((v_item.key, node))
            print points
            v_item = v_queue.pop()
    return points

if __name__ == '__main__':
    #h_lines, v_lines = generateLines(10)
    h_lines = [((9, 6), (2, 6)), ((3, 2), (9, 2)), ((8, 3), (9, 3)), ((6, 7), (9, 7)), ((4, 9), (3, 9)), ((4, 5), (8, 5)), ((9, 4), (4, 4)), ((2, 8), (4, 8)), ((8, 1), (2, 1)), ((1, 1), (4, 1))]
    v_lines = [((1, 7), (1, 0)), ((1, 2), (1, 6)), ((6, 9), (6, 3)), ((0, 6), (0, 6)), ((7, 3), (7, 0)), ((1, 4), (1, 9)), ((7, 6), (7, 0)), ((5, 1), (5, 1)), ((5, 3), (5, 7)), ((9, 0), (9, 8))]
    #print h_lines
    #print v_lines
    print find_cross(h_lines, v_lines)