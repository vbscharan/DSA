from typing import List


class Solution:
    def maxCoins(self, N : int, arr : List[int]) -> int:
        # code here
        dp=[[0 for _ in range(N+2)]for _ in range(N+2)]
        arr.insert(0,1)
        arr.append(1)
        for i in range(N,-1,-1):
            for j in range(1,N+1):
                if i>j:
                    continue
                maxi=-1
                for k in range(i,j+1):
                    maxi=max(maxi,(dp[i][k-1]+dp[k+1][j]+(arr[i-1]*arr[j+1]*arr[k])))
                dp[i][j]=maxi
        return dp[1][N]
                        
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxCoins(N, arr)
        
        print(res)
        

# } Driver Code Ends