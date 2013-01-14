#/user/bin/env python
'''
Created on 2013-1-8

@author: stefanie
'''
#import section

#global variable

#class definition
class ArrayAlgorithms(object):
    '''
    basic algorithms operating a array or several arrays.
    '''


    def __init__(self, array = range(1,10)):
        '''
        Constructor
        '''
        self.array = array
        
    def setArray(self, array):
        self.array = array
        
    def split_balance_arrays(self):
        '''
        Problem Introduction:
            There is a array contains several numbers, both positive and negative numbers, 
            Please split the array into two sub arrays which could make their sum is closest.
        Algorithm:
            calculate all the possible sum number of each subset, in order to avoid repeat calculation, 
            use a hash map to store all the sum and the list could get this sum.
            also have a variable monitor the closest sum to 1/2 total sum.
            iterate from 1..n, for each number have 2 cases:
                1. for each sum in sum hash map, could this new number create a new sum:
                    if YES, create a new entry in the map, and check if this sum is closest.
                2. also check if new number itself is in the map
                    if NOT, create a new entry in the map, and check if the sum is closest.
            after the iteration, the closest sum is captured, and the number list as the value in the map 
            which the key is the closest sum is one of the sub array. Then scan the array to remove all 
            the number in sub array to create the second sub array.
        '''
        array_sum = 0
        for num in self.array:
            array_sum += num
        print "Array sum is:", array_sum
        
        median = array_sum // 2     
        closestSum = 0
        sumDict = {}
        
        for num in self.array:
            temp_sumDict = sumDict.copy()
            for key, value in temp_sumDict.items():
                newSum = key + num
                if not(sumDict.has_key(newSum)):
                    newList = value[0:]
                    newList.append(num)
                    sumDict[newSum] = newList
                
                if abs(median - newSum) < abs(median - closestSum):
                    closestSum = newSum
            if not(sumDict.has_key(num)):
                sumDict[num] = [num]
                if abs(median - num) < abs(median - closestSum):
                    closestSum = num
        
        array1 = sumDict[closestSum]
        array2 = self.array[0:]
        for num in array1:
            array2.remove(num)
        
        
        print "Closest sum value is: ", closestSum
        print "Arrays are: ", array1, array2
        
    def subset_within_K(self, K):
        '''
        '''
        subsets = []
        
        for num in self.array:
            subsets = self._subset_within_K(K, num, subsets)
            
        for item in subsets:
            print item['set']
        
    def _subset_within_K(self, K, num, subset_previous):
        '''
        '''
        subset = subset_previous[0:]
        
        isAdded = False
        for item in subset_previous:
            isAdded = isAdded or self._process_one_node(item, num, K, subset, True)
            #print "num", num, "item", item['set'], isAdded
     
        if (not isAdded) and num <= K:
            item = {}
            item['set']= [num]
            item['sum']= num
            item['child'] = None
            subset.append(item) 
            
        return subset
    
    def _process_one_node(self, item, num, K, subset, isTop):
        newSum = item['sum'] + num
        if newSum <= K:
            newList = item['set'][0:]
            newList.append(num)
            newItem = {}
            newItem['set']= newList
            newItem['sum']= newSum
            newItem['child'] = item
            subset.append(newItem) 
            if(isTop):           
                subset.remove(item)
            return True
        else:
            if(item['child']):
                return self._process_one_node(item['child'], num, K, subset, False)
            else:
                return False
            
        
#function section
def test_split_balance_array():
    arrayAlgo = ArrayAlgorithms();
    print "Array is: ", arrayAlgo.array
    arrayAlgo.split_balance_arrays()

    arrayAlgo.setArray([1,2,3,4,1,1,1])
    print "Array is: ", arrayAlgo.array
    arrayAlgo.split_balance_arrays() 
    
def test_subset_within_K():
    arrayAlgo = ArrayAlgorithms();
    arrayAlgo.subset_within_K(10);

#main function
if __name__ == '__main__':
    #test_split_balance_array()
    test_subset_within_K()

           
                
            
            
            
            