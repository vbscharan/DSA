#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''
import heapq
class Solution:
    def __init__(self):
        self.heap1=[]
        self.heap2=[]
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        if len(self.heap1)+len(self.heap2)%2!=0:
            if len(self.heap1)<len(self.heap2):
                heapq.heappush(self.heap1,-1*heapq.heappop(self.heap2))
            if len(self.heap1)-len(self.heap2)>1:
                heapq.heappush(self.heap2,-1*heapq.heappop(self.heap1))
        

    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if len(self.heap1)==len(self.heap2):
            return (-self.heap1[0]+self.heap2[0])/2
        else:
            return -self.heap1[0]
        
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        if len(self.heap1)==0 and len(self.heap2)==0:
            self.heap1.append(-1*x)
            heapq.heapify(self.heap1)
        elif x<=self.getMedian():
            heapq.heappush(self.heap1,-1*x)
            self.balanceHeaps()
        elif x>self.getMedian():
            if len(self.heap2)==0:
                self.heap2.append(x)
                heapq.heapify(self.heap2)
            else:
                heapq.heappush(self.heap2,x)
            self.balanceHeaps()
            
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends