#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        st=[]
        for i in S:
            #print(st)
            if i.isdigit():
                st.append(int(i))
            else:
                if len(st)>1:
                    if i=='+':
                        st.append(st.pop(-1)+st.pop(-1))
                    elif i=='-':
                        st.append(-st.pop(-1)+st.pop(-1))
                    elif i=='*':
                        st.append(st.pop(-1)*st.pop(-1))
                    elif i=='/':
                        s=st.pop(-1)
                        f=st.pop(-1)
                        st.append(f//s)
        #print(st)
        return st.pop(-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

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
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends