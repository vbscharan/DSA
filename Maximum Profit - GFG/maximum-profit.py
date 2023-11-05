#User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        # code here
        '''
        dp=[[[-1 for _ in range(K)]for _ in range(2)] for _ in range(N)]
        def calp(ind,buy,k):
            if k<0 or ind==N:
                return 0
            if dp[ind][buy][k]!=-1:
                return dp[ind][buy][k]
            if buy:
                p= max(-A[ind]+calp(ind+1,0,k),calp(ind+1,1,k))
            else:
                p= max(A[ind]+calp(ind+1,1,k-1),calp(ind+1,0,k))
            dp[ind][buy][k]=p
            return dp[ind][buy][k]
        return calp(0,1,K-1)
        '''
        dp=[[[0 for _ in range(K+1)]for _ in range(2)] for _ in range(N+1)]
        for ind in range(N-1,-1,-1):
            for buy in range(2):
                for k in range(1,K+1):
                    if buy:
                        p= max(-A[ind]+dp[ind+1][0][k],dp[ind+1][1][k])
                    else:
                        p= max(A[ind]+dp[ind+1][1][k-1],dp[ind+1][0][k])
                    dp[ind][buy][k]=p
        return dp[0][1][K]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends