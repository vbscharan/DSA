# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        # Code here
        dp=[[-1 for _ in range(len(string)+1)] for _ in range(len(pattern)+1)]
        def smatch(i,j):
            if i<0 and j<0:
                return True
            if i<0 and j>=0:
                return False
            if j<0 and pattern[i]=='*':
                for k in range(i+1):
                    if pattern[k]!='*':
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if pattern[i]==string[j] or pattern[i]=='?':
                dp[i][j]= smatch(i-1,j-1)
                return dp[i][j]
            if pattern[i]=='*':
                dp[i][j]= smatch(i-1,j) or smatch(i,j-1)
                return dp[i][j]
            dp[i][j]=False
            return dp[i][j]
        return smatch(len(pattern)-1,len(string)-1)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends