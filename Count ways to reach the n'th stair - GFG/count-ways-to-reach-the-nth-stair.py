#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # code here
        if n==0:
            return 1
        elif n==1:
            return 1
        elif n==2:
            return 2
        dp=[0]*(n+1)
        dp[0]=0;dp[1]=1;dp[2]=2
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2])%1000000007
        return dp[n]

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