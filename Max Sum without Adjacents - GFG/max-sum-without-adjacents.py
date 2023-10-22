#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		'''
		dp=[-1 for _ in range(n+1)]
		def fun(ind):
		    if ind==0:
		        return arr[ind]
	        if ind<0:
	            return 0
            if dp[ind]!=-1:
                return dp[ind]
            take=arr[ind]+fun(ind-2)
            notake=fun(ind-1)
            dp[ind]= max(take,notake)
            return dp[ind]
        return fun(n-1)
        '''
        dp=[0 for _ in range(n)]
        dp[0]=arr[0]
        for i in range(1,n):
            take=arr[i]
            if i>1:
                take+=dp[i-2]
            dp[i]=max(take,dp[i-1])
        return dp[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends