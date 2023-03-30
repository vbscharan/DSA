#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        if len(str1)!=len(str2):
            return 0
        if len(str1)<=2:
            return 0
        k=len(str1)
        start=2
        j=0
        if str1[0]==str2[-2]:
            while start<k and j<k:
                if str1[start]==str2[j]:
                #print(str1[start])
                #print(str2[j])
                    start+=1
                    j+=1
                else:
                    return 0
                if start==(k-1):
                    start=(start)%k
                #j+=1
            return 1
        #print(str1)
        #start=2
        #j=0
        else:
            while start<k and j<k:
                if str1[j]==str2[start]:
                    start+=1
                    j+=1
                else:
                    return 0
                if start==(k-1):
                    start=(start)%k
            return 1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends