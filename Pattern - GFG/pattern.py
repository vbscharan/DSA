#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1,N+1):
            for j in range(N-i,0,-1):
                print("",end=" ")
            for k in range(i):
                print("*",end=" ")
            print()
        for i in range(N+1,1,-1):
            for k in range(N+1-i):
                print(" ",end="")
            for j in range(i,1,-1):
                print("*",end=" ")
            print()    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends