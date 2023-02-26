#User function Template for python3

class Solution:
    def isKSortedArray(self, arr, n, k): 
        #code here.
        a=sorted(arr)
        #print(a)
        def Binarysearch(a,x):
            l=0;h=n-1
            while l<=h:
                mid=(l+h)//2
                if a[mid]==x:
                    return mid
                elif x<a[mid]:
                    h=mid-1
                else:
                    l=mid+1
        for i in range(n):
            if abs(i-Binarysearch(a,arr[i]))<=k:
                continue
            else:
                return "No"
        return "Yes"



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    ob = Solution()
    print(ob.isKSortedArray(a, n, k))

# } Driver Code Ends