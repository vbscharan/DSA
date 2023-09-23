#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        # code here
        s1=S
        s2=S[::-1]
        dp=[[0]*(len(s1)+1) for _ in range(len(s2)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 or j==0:
                    dp[i][j]=0
                    continue
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(s1)][len(s1)]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends