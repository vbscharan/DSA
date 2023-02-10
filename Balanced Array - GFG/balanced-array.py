#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        i=0
        j=n-1
        k1=k2=0
        while i<j:
            k1+=a[i]
            k2+=a[j]
            i+=1;j-=1
        return abs(k1-k2)
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends