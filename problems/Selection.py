'''
Created on 2013-3-15

@author: stefanie
'''

'''
Problem: given a array, find the Kth largest number in the array
Solution: 
    using QuickSort main idea, to partition the array into two part, and recursively find the Kth number
'''

def selection(array, k):
    return select(array, 0, len(array) -1, k);
    
def select(array, low, high, k):
    mid = partition(array, low, high)
    index = high - k + 1
    if mid == index:
        return array[mid], mid
    elif mid < index:
        return select(array, mid+1, high, k)
    else:
        return select(array, low, mid-1, k-(high-mid+1))
       

def partition(array, low, high):
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

if __name__ == '__main__':
    array = [79, 82, 23, 50, 17, 53, 37, 89, 60, 14]
    print array
    for i in range(1,len(array)+1):
        value, index = selection(array, i);
        print i,'th num:', value
        print 'top ', i, ' num: ', array[index:len(array):1]