#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		su=sum(arr)
		dp=[[0]*((su//2)+1) for _ in range(n+1)]
		for i in range((su//2)+1):
		    dp[0][i]=False
	    for i in range(n+1):
	        dp[i][0]=True
        for i in range(1,n+1):
            for j in range((su//2)+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        mini=float('inf')
        for i in range((su//2)+1):
            if dp[-1][i]==True:
                mini=min(mini,(su-2*i))
        return mini
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends