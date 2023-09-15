import sys
sys.setrecursionlimit(10**6)
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        dp=[-1]*(n+1)
        dp[1]=1;dp[2]=1
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2])% 1000000007
        return dp[n]
        '''
        def nFib(n):
            if n==1 or n==2:
                dp[n]=1
                return 1
            if dp[n]!=-1:
                return dp[n]
            else:
                dp[n]=(nFib(n-1)+nFib(n-2))% 1000000007
                return dp[n]
        return nFib(n)
        '''
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends