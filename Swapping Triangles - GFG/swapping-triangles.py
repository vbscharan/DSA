#User function Template for python3

class Solution:
    def swapTriangle(self,N,A):
        #code here
        for i in range(N):
            for j in range(i,N):
                #print(A[j][i],end=" ")
            #print()
                A[j][i],A[i][j]=A[i][j],A[j][i]
        return A

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        A=[[0]*N]*N
        for i in range(N):
            A[i]=list(map(int,input().strip().split(" ")))
        ob=Solution()
        ans=ob.swapTriangle(N,A)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()    
# } Driver Code Ends