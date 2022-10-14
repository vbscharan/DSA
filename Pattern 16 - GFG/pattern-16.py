#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        k=ord('A')
        for i in range(1,N+1):
            for j in range(i):
                print(chr(k),end="")
            print()
            k+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends