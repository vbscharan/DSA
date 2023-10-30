#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        
        su=sum(arr)
        if (su-d)<0 or ((su-d)%2!=0):
            return 0
        k=(su-d)//2
        dp=[[-1 for _ in range(k+1)] for _ in range(n+1)]
        def calCount(ind,tar):
            if ind==0:
                if tar==0 and arr[ind]==0:
                    return 2
                if tar==0 or arr[ind]==tar:
                    return 1
                return 0
            if dp[ind][tar]!=-1:
                return dp[ind][tar]%1000000007
            take=0
            if arr[ind]<=tar:
                take=calCount(ind-1,tar-arr[ind])
            notake=calCount(ind-1,tar)
            dp[ind][tar] =(take+notake)%1000000007
            return dp[ind][tar]
        return calCount(n-1,k)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends