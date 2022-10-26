#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        k=n*(n+1)//2
        s1=sum(array)
        #0
        #for i in array:
        #    s1+=i
        return k-s1


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends