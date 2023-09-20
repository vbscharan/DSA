#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp=[[0]*(m+1) for _ in range(n+1)]
        maxi=float('-inf')
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif S1[i-1]==S2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    #dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    dp[i][j]=0
                maxi=max(dp[i][j],maxi)
        return maxi
        for i in dp:
            print(i)
        if dp[n][m-1]:
            return dp[n][m-1]
        return dp[n-1][m]
        for i in dp:
            print(i)
        return dp[n][m-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends