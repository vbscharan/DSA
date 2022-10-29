#User function Template for python3

class Solution:
    def revCoding(self, n, m):
        # code here
        if (n*(n+1))//2==m:
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.revCoding(n,m))
# } Driver Code Ends