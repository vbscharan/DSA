#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        dp=[[-1 for _ in range(N)]for _ in range(N)]
        def maxSumPath(r,c):
            if r<0 or r>N-1 or c<0 or c>N-1:
                return 0
            if r==N-1:
                return Matrix[r][c]
            if dp[r][c]!=-1:
                return dp[r][c]
            #maxi=float('-inf')
            dp[r][c]= Matrix[r][c]+max(maxSumPath(r+1,c),maxSumPath(r+1,c-1),maxSumPath(r+1,c+1))
            return dp[r][c]
        maxi=float('-inf')
        for i in range(N):
            maxi=max(maxi,maxSumPath(0,i))
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends