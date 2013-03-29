from __future__ import division
from collections import deque
import string
'''
Created on Mar 27, 2013

@author: stefaniezhao
'''

class Graph(object):
    '''
    the implementation of Graph using adjacency-list
    '''


    def __init__(self):
        self.adj = {}
        self.edge = 0
        
    def _addToADJ(self, src, tar):
        adj = None
        if src not in self.adj:
            adj = []
            self.adj[src] = adj
        else:
            adj = self.adj[src]
        if tar not in adj:
            adj.append(tar)
        
    def _removeFromADJ(self, src, tar):
        adj = self.adj[src]
        adj.remove(tar)
        
    def addEdge(self, v, w):
        self._addToADJ(v, w)
        self._addToADJ(w, v)
        self.edge += 1
        
    def removeEdge(self, v, w):
        self._removeFromADJ(v, w)
        self._removeFromADJ(w, v)
        self.edge -= 1
        
    def adj_list(self, v):
        return self.adj[v]
        
    def V(self):
        return len(self.adj)
    
    def vetices(self):
        return self.adj.keys()

    def E(self):
        return self.edge

    def all_edges(self):
        edges = []
        for v in self.vetices():
            for w in self.adj_list(v):
                print edges.append((w,v))
                
        return edges
    
    def print_adj(self):
        for v in self.vetices():
            print v, ": ", self.adj_list(v)
    
    @staticmethod
    def degree(graph, v):
        return len(graph.adj_list(v))
    
    @staticmethod
    def maxDegree(graph):
        maxDegree = 0
        for v in graph.vetices():
            degree = len(graph.adj_list(v))
            if degree > maxDegree:
                maxDegree = degree
        return maxDegree
    
    @staticmethod
    def averageDegree(graph):
        return 2* graph.E()/graph.V()
    
    @staticmethod
    def numberOfSelfLoop(graph):
        count = 0
        for v in graph.vetices():
            for w in graph.adj_list(v):
                if v == w: 
                    count+= 1
        return count /2
    
class DepthFirstPaths(object):
    
    '''
        the implementation of depth first search on Graph from a certain vertex
        DFS marks all vertices connected to s in time proportional to the sum of their degrees
        After DFS, can find vertices connected to s in constant time and can find a path to s in time proportional to its length
    '''
    
    def __init__(self, graph, v):
        self.graph = graph
        self.marked = {}
        self.edgeTo = {}
        self.s = v
        
        
    def search(self):
        self._search(self.s)
        
    def _search(self, v):
        self.marked[v] = True
        print v
        for w in self.graph.adj_list(v):
            if w not in self.marked or not self.marked[w]:
                self._search(w)
                self.edgeTo[w] = v
    
    def hasPathTo(self, v):
        return self.marked[v]
    
    def path(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path
        
  
class BreathFirstPaths(DepthFirstPaths):
    
    '''
        the implementation of breath first search of a graph on certain vertex
        BFS computes shortest paths from s to all other vertices in a graph in time proportional to E+V
    '''
        
    def search(self, v):
        queue = deque([])
        queue.append(v)
        self.marked[v] = True
        while len(queue) > 0:
            s = queue.popleft()
            print s
            for w in self.graph.adj_list(s):
                if w not in self.marked or not self.marked[w]:
                    queue.append(w)
                    self.marked[w] = True
                    self.edgeTo[w] = s
                    
class ConnectedComponent(object):
    
    def __init__(self, graph):
        self.graph = graph
        self.marked = {}
        self.id = {}
        self.count = 0
        
    def build(self):
        for v in self.graph.vetices():
            if v not in self.marked or not self.marked[v]:
                self.count += 1
                self._dfs(v)
                
    def _dfs(self, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in self.graph.adj_list(v):
            if w not in self.marked or not self.marked[w]:
                self._dfs(w)
        
    def connected(self, v, w):
        return self.id[v] == self.id[w]
        
    def count(self):
        return self.count
        
    def component_id(self, v):
        return self.id[v]
    
def parseGraph(str):
    graph = Graph()
    for edge in str.split(" "):
        nodes = edge.split("-")
        graph.addEdge(nodes[0], nodes[1])
    return graph

def testcase():
    str = "A-E A-F B-G B-C C-G D-H D-G F-G G-H"
    graph = parseGraph(str)
    dfs = DepthFirstPaths(graph, "A")
    dfs.search()
    
def testcase2():
    str = "A-B B-E C-D C-G C-F B-F G-H D-G D-H F-G"
    graph = parseGraph(str)
    graph.print_adj()
    bfs = BreathFirstPaths(graph, "A")
    bfs.search("A")
    
def testcase3():
    str = "A-F B-G B-H I-J D-J C-D C-I D-I J-E D-E G-H"
    graph = parseGraph(str)
    graph.print_adj()
    cc = ConnectedComponent(graph)
    cc.build()
    
    for char in string.uppercase[:10]:
        print char, cc.component_id(char)
    
    
if __name__ == '__main__':
    testcase3()
                    
            