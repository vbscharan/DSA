#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        if N==1:
            return 1
        dp=[1 for _ in range(N)]
        lis=[i for i in range(N)]
        le=1
        index=0
        for ind in range(N):
            for prev in range(ind):
                if arr[prev]<arr[ind] and 1+dp[prev]>dp[ind]:
                    dp[ind]=1+dp[prev]
                    lis[ind]=prev
            if dp[ind]>le:
                le=dp[ind]
                index=ind
        ans=[]
        ans.append(arr[index])
        while lis[index]!=index:
            index=lis[index]
            ans.append(arr[index])
        return ans[::-1]
                    
        
        
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longestIncreasingSubsequence(N, arr)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends