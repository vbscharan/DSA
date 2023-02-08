
#User function Template for python3

class Solution:
    
    #Function to find minimum number of characters which Ishaan must insert  
    #such that string doesn't have three consecutive same characters.
    def modified(self,s):
        #code here
        k=0
        i=1
        while i<(len(s)-1):
            if s[i-1]==s[i] and s[i]==s[i+1]:
                k+=1
                i+=1
            i+=1
        return k


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
        obj = Solution()
        print(obj.modified(s))
# } Driver Code Ends