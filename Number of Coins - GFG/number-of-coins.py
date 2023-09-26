#User function Template for python3
class Solution:
	def minCoins(self, coins, M, V):
		# code here
        dp=[[float('inf') for _ in range(V+1)] for _ in range(M+1)]
        for i in range(1,M+1):
            dp[i][0]=0
        for j in range(1,V+1):
            if j%coins[0]==0:
                dp[1][j]=j
            else:
                dp[1][j]=float('inf')
        #print(dp[:][0])
        for i in range(1,M+1):
            for j in range(1, V+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i-1][j] , 1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        #print(dp[:][-1])
        if dp[-1][-1]==float('inf'):
            return -1
        return dp[-1][-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends