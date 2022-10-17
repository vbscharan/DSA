#User function Template for python3

class Solution:
    def EvenOddSum(self,N,Arr):
        #code here (return list)
        even=sum([i for i in Arr[1::2]])
        odd=sum([i for i in Arr[0::2]])
        return odd,even

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        ans=ob.EvenOddSum(N,Arr)
        print(ans[0],end=" ")
        print(ans[1])
# } Driver Code Ends