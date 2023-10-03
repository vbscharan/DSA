#User function Template for python3

class Solution:
    def countMin(self, Str):
        # code here
        n=len(Str)
        dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if Str[i-1]==Str[n-j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends