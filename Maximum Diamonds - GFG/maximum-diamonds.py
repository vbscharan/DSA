#User function Template for python3
import heapq
import math
class Solution:
    def maxDiamonds(self, A, N, K):
        # code here
        A=[-1*i for i in A]
        heapq.heapify(A)
        sum=0
        for i in range(K):
            k=heapq.heappop(A)
            sum+=(-1*k)
            k=-k//2
            heapq.heappush(A,-k)
            
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends