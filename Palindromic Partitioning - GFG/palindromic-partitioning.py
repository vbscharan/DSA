#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        n=len(string)
        dp=[0 for _ in range(n+1)]
        def isPalindrome(x,y):
            while x<y:
                if string[x]!=string[y]:
                    return False
                x+=1
                y-=1
            return True
        for i in range(n-1,-1,-1):
            mini=float('inf')
            for j in range(i,n):
                if isPalindrome(i,j):
                    ways=1+dp[j+1]
                    mini=min(mini,ways)
            dp[i]=mini
        return dp[0]-1
        '''
        def pp(i,j):
            if i>j or isPalindrome(i,j):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for k in range(i,j):
                if dp[i][k]!=-1:
                    left=dp[i][k]
                else:
                    left=pp(i,k)
                if dp[k+1][j]!=-1:
                    right=dp[k+1][j]
                else:
                    right=pp(k+1,j)
                mini=min(mini,1+left+right)
            dp[i][j]=mini
            return dp[i][j]
        return pp(0,n-1)
        '''
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends