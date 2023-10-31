#User function Template for python3

class Solution:
    def findTargetSumWays(self, arr, N, target):
        # code here 
        su=sum(arr)
        if (su-target)<0 or (su-target)%2!=0:
            return 0
        k=(su-target)//2
        dp=[[-1 for _ in range(k+1)] for _ in range(N+1)]
        def findTarget(ind,k):
            if ind==0:
                if k==0 and arr[0]==0:
                    return 2
                elif k==0 or arr[0]==k:
                    return 1
                return 0
            if dp[ind][k]!=-1:
                return dp[ind][k]
            notake=findTarget(ind-1,k)
            take=0
            if arr[ind]<=k:
                take=findTarget(ind-1,k-arr[ind])
            dp[ind][k]= take+notake
            return dp[ind][k]
        return findTarget(N-1,k)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends