#User function Template for python3

class Solution:
	def MinCoin(self, nums, amount):
		# Code here
		dp=[[-1 for _ in range(amount+1)] for _ in range(len(nums)+1)]
		k=100000
		for i in range(amount+1):
		    dp[0][i]=k
	    for i in range(len(nums)+1):
	        dp[i][0]=0
        for i in range(1,amount+1):
            if i%nums[0]==0:
                dp[1][i]=i
            else:
                dp[1][i]=0
        for i in range(1,len(nums)+1):
            for j in range(1,amount+1):
                if nums[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-nums[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        #for i in dp:
         #   print(i)
        if dp[-1][-1]<=0 or dp[-1][-1]==k:
            return -1
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, amount = input().split()
		n = int(n)
		amount = int(amount)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.MinCoin(nums, amount)
		print(ans)
# } Driver Code Ends