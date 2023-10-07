#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        dp=[-1 for _ in range(n+1)]
        def cou(i):
            if i==0:
                return 1
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]= (cou(i-1)+cou(i-2)+cou(i-3))%1000000007
            return dp[i]
        return cou(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends