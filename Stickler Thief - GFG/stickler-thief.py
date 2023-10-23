#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        '''
        dp=[-1 for _ in range(n)]
        def maxSum(ind):
            if ind==0:
                return a[ind]
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            take=a[ind]+maxSum(ind-2)
            notake=maxSum(ind-1)
            dp[ind]=max(take,notake)
            return dp[ind]
        return maxSum(n-1)
        '''
        dp=[0 for _ in range(n)]
        dp[0]=a[0]
        for i in range(1,n):
            #f=float('inf')
            f=a[i]
            if i>1:
                f+=dp[i-2]
            s=dp[i-1]
            dp[i]=max(f,s)
        return dp[n-1]
            


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
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends