#User function Template for python3

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        #code here
        dic={}
        for i in range(len(Str)):
            if dic.get(Str[i])!=None:
                dic[Str[i]][0]=dic[Str[i]][0]+1
                dic[Str[i]][1]=min(i,dic[Str[i]][1])
            else:
                dic[Str[i]]=[1,i]
        k=len(Str);cut=0
        for i in pat:
            if dic.get(i)!=None:
                if dic[i][1]<k:
                    cut=1
                    k=dic[i][1]
        if cut:
            return k
        return -1
        #print(dic)
            


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
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        print(ans)
# } Driver Code Ends