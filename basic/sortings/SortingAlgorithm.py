'''
Created on 2013-1-14

@author: stefanie
'''
import copy

class SortingAlgorithm(object):
    
    def __init__(self, array = range(1,10)):
        '''
        Constructor
        '''
        self.array = array
    
    def bottom_bubble(self):
        array = copy.copy(self.array)
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        return array
                    
    def top_bubble(self):
        array = copy.copy(self.array)
        for i in range(1, len(array)):
            for j in range(0, i):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
        return array;
    
    def selection_sorting(self):
        array = copy.copy(self.array)
        for i in range(0, len(array)):
            min_index = i
            for j in range(i, len(array)):
                if(array[j] < array[min_index]):
                    min_index = j
            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]
        return array
    
    def insertion_sorting(self):
        array = copy.copy(self.array)
        for i in range(1, len(array)):
            for j in (range(1, i + 1)[::-1]):
                if(array[j] < array[j - 1]):
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    break
        return array
    
    def shell_sorting(self):
        array = copy.copy(self.array)
        h = 1
        while h < len(array)/3:
            h=3*h+1;
            
        while h >= 1:
            for i in range(h, len(array)):
                for j in range(h, i+1)[::-h]:
                    if(array[j] < array[j-h]):
                        array[j], array[j-h] = array[j-h], array[j]
            h = h/3;
            #print array
        return array;
    
    def quick_sorting(self):
        array = copy.copy(self.array)
    
    def division_merge(self):
        array = copy.copy(self.array)
        self._division(array, 0, len(array) -1)
        return array
    
    def _division(self, array, begin, end):
        if begin < end:
            index = (begin + end) / 2
            self._division(array, begin, index)
            self._division(array, index + 1, end)
            self._merge(array, begin, index, end)
        
    def _merge(self, array, begin, index, end):
#        print begin, index, end
        result = range(0, end-begin+1)
        i = begin; j = index + 1; k = 0
        while i <= index and j <= end:
            if array[i] < array[j]:
                #print k, i
                result[k] = array[i]
                i += 1
            else :
                result[k] = array[j]
                j += 1
            k += 1
        while i <= index:
            result[k] = array[i]
            k += 1; i += 1
        while j <= end:
            result[k] = array[j]
            k += 1; j += 1
        #print array, result
        array[begin:end + 1] = result
        #print array
        
    def quicksort(self):
        array = copy.copy(self.array)
        self.quick_sort(array,0,len(array)-1)
        return array
    
    def quick_sort(self, array, low, high):
        if low >= high:
            return
        mid = self.partition_2(array, low, high)
        self.quick_sort(array, low, mid -1)
        self.quick_sort(array, mid + 1, high)
        
    def partition(self, array, low, high):
        i = low+1 
        j = high
        key = array[low]
        while True:
            while array[i] < key and i < high:
                i += 1
            while array[j] > key and j > low:
                j -= 1
            if i >= j:
                break
            array[i], array[j] = array[j], array[i]
        array[low], array[j] = array[j], array[low]
        return j
    
    def partition_2(self, array, low, high):
        key = array[high]
        j = low
        i = low -1
        while j < high:
            if array[j] < key:
                i += 1
                array[i], array[j] = array[j], array[i]
            j += 1
        i += 1
        array[high], array[i] = array[i], array[high]
        return i
        
        
                       
#main function
if __name__ == '__main__':
    #test_split_balance_array()
    #array = [2,34,4,23,67,1,7,19]
    array = [79, 82, 23, 50, 17, 53, 37, 89, 60, 14]
    
    print array    
    sorting = SortingAlgorithm(array)
   
    print "Top Bubble Result: ", sorting.top_bubble()
    print "Button Bubble Result: ", sorting.bottom_bubble()
    print "Merge Sorting Result: ", sorting.division_merge()
    print "Selection Sorting Result: ", sorting.selection_sorting()
    print "Insertion Sorting Result: ", sorting.insertion_sorting()
    print "Shell Sorting Result: ", sorting.shell_sorting()
    print "Quick Sorting Result: ", sorting.quicksort()
    
    