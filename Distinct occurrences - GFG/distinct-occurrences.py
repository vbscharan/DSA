# Your task is to complete this function
# Finction should return Integer
class Solution:
    def sequenceCount(self,arr1, arr2):
        # Code here
        dp=[[-1 for _ in range(len(arr2))] for _ in range(len(arr1))]
        def count(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if arr1[i]==arr2[j]:
                dp[i][j]= (count(i-1,j-1)+count(i-1,j))%1000000007
                return dp[i][j]
            else:
                dp[i][j]= count(i-1,j)%1000000007
                return dp[i][j]
        return count(len(arr1)-1,len(arr2)-1)

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends