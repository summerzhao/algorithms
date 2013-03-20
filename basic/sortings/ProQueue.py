'''
Created on 2013-3-17

@author: stefanie
'''

class QueueNode(object):
    def __init__(self, key, value=None):
        self.key = key
        if value == None:
            self.value = key
        else:
            self.value = value

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
            node = array[i]
            if isinstance(node, QueueNode):
                self.array.append(node)
            else:
                self.array.append(QueueNode(node))
            
        for i in range(1, self.n)[::-1]:
            self._sink(i)
            
    def get_keys(self):
        array = []
        for i in range(1, self.size()+1):
            array.append(self.array[i].key)
        return array
        
    def size(self):
        return self.n
    
    '''
     the element will swim up if its parent is smaller than it, exchange it with its parent
    '''
    def _swim(self, i):
        while i / 2 > 0:
            if self.array[i].key > self.array[i / 2].key:
                self.array[i], self.array[i / 2] = self.array[i / 2], self.array[i]
            i = i / 2
                
    def _get_larger_child(self, i):
        if i * 2 + 1 <= self.n:
            if self.array[i * 2 + 1].key > self.array[i * 2].key:
                return i * 2 + 1
        return i * 2
                
    '''
    the element will sink down if its child is larger than it, exchange the larger child with it.
    '''
    def _sink(self, i):
        while 2 * i <= self.n:
            max_child = self._get_larger_child(i)
            if self.array[max_child].key > self.array[i].key:
                self.array[max_child], self.array[i] = self.array[i], self.array[max_child]
            i = max_child
    
    '''
    add a new element, add the element to the end of the binary heap, and let it swim up
    '''
    def push(self, item):
        self.n += 1
        self.array.append(item)
        self._swim(self.n)
        
    def max(self):
        if self.n > 0:
            return self.array[1]
        
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
    queue.push(QueueNode(76))
    queue.push(QueueNode(5))
    queue.push(QueueNode(45))
    queue.push(QueueNode(90))
    
    print queue.pop().value  # 90
    print queue.pop().value  # 76
    print queue.pop().value  # 45
    print queue.pop().value  # 5

def testcase2():
    queue = ProQueue()
    array = [9, 9, 9, 8, 8, 9, 9, 6, 4, 3, 3, 4, 8, 4, 4, 2, 2, 2, 4]
    for node in array:
        queue.push(QueueNode(node))
        
    print queue.get_keys()
        
if __name__ == '__main__':
    testcase1()       
            
    
        
