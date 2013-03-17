'''
Created on 2013-3-17

@author: stefanie
'''

class ProQueue(object):
    '''
    the binary heap implementation
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.array = []
        self.array.append(0)
        self.n = 0
        
    def init_by_array(self, array):
        self.n = len(array)
        for i in range(0, self.n):
            self.array.append(array[i])
            
        for i in range(1, self.n)[::-1]:
            self._sink(i)
        
        
    def size(self):
        return self.n
    
    '''
     the element will swim up if its parent is smaller than it, exchange it with its parent
    '''
    def _swim(self, i):
        while i/2 > 0:
            if self.array[i] > self.array[i/2]:
                self.array[i], self.array[i/2] = self.array[i/2], self.array[i]
            i = i/2
                
    def _get_larger_child(self, i):
        left = self.array[i*2]
        if i*2 + 1 <= self.n:
            right = self.array[i*2+1]
            if right > left:
                return i*2+1
        return i*2
                
    '''
    the element will sink down if its child is larger than it, exchange the larger child with it.
    '''
    def _sink(self, i):
        while 2*i <= self.n:
            max_child = self._get_larger_child(i)
            if self.array[max_child] > self.array[i]:
                self.array[max_child], self.array[i] = self.array[i], self.array[max_child]
            i = max_child
    
    '''
    add a new element, add the element to the end of the binary heap, and let it swim up
    '''
    def push(self, item):
        self.n += 1
        self.array.append(item)
        self._swim(self.n)
        
    '''
    delete a largest element, exchange it with the end of the heap, and let the element sink down.
    '''
    def pop(self):
        if self.n > 0:
            item = self.array[1]
            self.array[1] = self.array[self.n]
            del self.array[self.n]
            self.n -= 1
            self._sink(1);
            return item

def testcase1():
    queue = ProQueue()
    queue.push(76)
    queue.push(5)
    queue.push(45)
    queue.push(90)
    
    print queue.pop() #90
    print queue.pop() #76
    print queue.pop() #45
    print queue.pop() #5

def testcase2():
    array = [92, 78, 79, 68, 75, 31, 76, 45, 54, 58]
    queue = ProQueue()
    queue.init_by_array(array)
    print queue.array
    queue.push(17)
    queue.push(40)
    queue.push(22)
    print queue.array
    
def testcase3():
    array = [99, 90, 31, 84, 70, 18, 24, 27, 63, 41]
    queue = ProQueue()
    queue.init_by_array(array)
    print queue.array
    print queue.pop()
    print queue.pop()
    print queue.pop()
    print queue.array
    
def testcase4():
    array = [94, 73, 13, 32, 75, 16, 20, 28, 80, 76]
    queue = ProQueue()
    queue.init_by_array(array)
    print queue.array
        
if __name__ == '__main__':
    testcase4()       
            
    
        