#User function Template for python3


class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        i=0;j=n-1
        c=0
        while i<j:
            if arr[i]+arr[j]==sum:
                c+=1
                i+=1
                j-=1
            elif arr[i]+arr[j]<sum:
                i+=1
            elif arr[i]+arr[j]>sum:
                j-=1
        if c==0:
            return -1
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends