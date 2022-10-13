#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        k=['GFG']*n
        for i in k:
            print(i,end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
# } Driver Code Ends