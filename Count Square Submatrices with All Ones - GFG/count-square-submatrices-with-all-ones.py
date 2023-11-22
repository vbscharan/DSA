#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countSquares(self, N, M, matrix):
        # Code here
        su=sum(matrix[0])
        for i in range(1,N):
            for j in range(1,M):
                if matrix[i][j]==1:
                    matrix[i][j]=1+min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
                else:
                    matrix[i][j]=0
            su+=sum(matrix[i])
        return su

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, M = list(map(int, input().split()))
        matrix = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.countSquares(N, M, matrix)
        print(res)
# } Driver Code Ends