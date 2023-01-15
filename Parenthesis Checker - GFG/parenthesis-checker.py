class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        k=[]
        for i in x:
            if i=='(' or i=='[' or i=='{':
                k.append(i)
            else:
                if len(k)==0:
                    return False
                l=k.pop()
                if (i=='}' and l=='{') or (i==']' and l=='[') or (i==')' or l==')'):
                    continue
                return False
        if len(k)==0:
            return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends