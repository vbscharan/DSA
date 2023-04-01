#User function Template for python3

class Solution:
    def minRow(self,N,M,A):
        #code here
        mini=0;row=0
        for i in range(N):
            c=0
            for j in range(M):
                if A[i][j]==1:
                    c+=1
                if i==0:
                    mini=c
            if c<mini:
                mini=c
                row=i
        return row+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends