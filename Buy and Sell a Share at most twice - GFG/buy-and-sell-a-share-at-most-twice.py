from typing import List
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        '''
        dp=[[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n) ]
        def f(ind,buy,k):
            if ind==n or k==0:
                return 0
            if dp[ind][buy][k]!=-1:
                return dp[ind][buy][k]
            if buy:
                p=max(-price[ind]+f(ind+1,0,k),f(ind+1,1,k))
            else:
                p=max(price[ind]+f(ind+1,1,k-1),f(ind+1,0,k))
            dp[ind][buy][k]= p
            return dp[ind][buy][k]
        return f(0,1,2)
        '''
        #dp=[[[0 for _ in range(3)]for _ in range(2)]for _ in range(n+1) ]
        dp=[[0 for _ in range(5)]for _ in range(n+1)]
        transaction=0
        for ind in range(n-1,-1,-1):
            for transaction in range(3,-1,-1):
                if transaction%2==0:
                    p=max(-price[ind]+dp[ind+1][transaction+1],dp[ind+1][transaction])
                else:
                    p=max(price[ind]+dp[ind+1][transaction+1],dp[ind+1][transaction])
                dp[ind][transaction]=p
        return dp[0][0]
                    
        



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
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends