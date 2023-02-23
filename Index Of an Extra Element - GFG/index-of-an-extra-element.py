class Solution:
    def findExtra(self,a,b,n):
        #add code here
        def BinarySearch(arr,x):
            l=0;h=len(arr)-1
            mid=(l+h)//2
            while l<=h:
                if arr[mid]==x:
                    return True
                elif x<arr[mid]:
                    h=mid-1
                else:
                    l=mid+1
                mid=(l+h)//2
            return False
        for i in range(n):
            if BinarySearch(b,a[i]):
                continue
            else:
                return i


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends