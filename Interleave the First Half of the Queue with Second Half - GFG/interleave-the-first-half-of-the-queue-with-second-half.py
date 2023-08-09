
from typing import List


class Solution:
    def rearrangeQueue(self, N : int, q : List[int]) -> List[int]:
        # code here
        if N==2:
            return q
        ar=[]
        br=[]
        while len(q):
            if len(q)>N//2:
                a=q.pop(0)
                ar.append(a)
            else:
                b=q.pop(0)
                br.append(b)
        m=[]
        for i in range(len(ar)):
            m.append(ar[i])
            m.append(br[i])
        return m
        



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
        
        
        q=IntArray().Input(N)
        
        obj = Solution()
        res = obj.rearrangeQueue(N, q)
        
        IntArray().Print(res)
        

# } Driver Code Ends