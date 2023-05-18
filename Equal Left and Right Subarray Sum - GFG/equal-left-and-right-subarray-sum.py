# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        rightsum=0
        i=N-1
        leftsum=sum(A)-A[i]
        while i>=0:
            #print(A[i])
            #print(leftsum,rightsum)
            if rightsum!=leftsum:
                rightsum+=A[i]
                leftsum-=A[i-1]
                i-=1
            else:
                return i+1
                
        return -1
                



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends