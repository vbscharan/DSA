#User function Template for python3

class Solution:
    def mthHalf(self, N, M):
        # code here
        k=1
        while k<=(M-1):
            if N==0:
                return 0
            N//=2
            k+=1
        return N


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.mthHalf(N, M))
# } Driver Code Ends