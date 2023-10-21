#User function Template for python3

class Solution:
    def countWays(self, S1, S2):
        # code here 
        dp=[[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
        for i in range(len(S1)+1):
            dp[i][0]=1
        for i in range(1,len(S1)+1):
            for j in range(1,len(S2)+1):
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        S1 = input()
        S2 = input()
        ob = Solution()
        ans = ob.countWays(S1,S2)
        print(ans)
# } Driver Code Ends