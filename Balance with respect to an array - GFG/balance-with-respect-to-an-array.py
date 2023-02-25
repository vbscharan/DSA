#User function Template for python3
def NextSmallElement(arr,x):
    l=0;h=len(arr)-1
    index=0
    while l<=h:
        mid=(l+h)//2
        if a[mid]<x:
            l=mid+1
            #h=mid-1
            index=a[mid]
        elif a[mid]==x:
            return a[mid]
        else:
            #l+=1
            h=mid-1
    return index 
def NextGreaterElement(arr,x):
    l=0;h=len(arr)-1
    index=0
    while l<=h:
        mid=(l+h)//2
        if a[mid]>x:
            #l=mid+1
            h=mid-1
            index=a[mid]
        elif a[mid]==x:
            return a[mid]
        else:
            l=mid+1
            #h=mid-1
    return index
    #return a[index]
        

class Solution:
    def isBalanced(self,a,n,x):
        f1=NextSmallElement(a,x)
        f2=NextGreaterElement(a,x)
        #print(f1)
        #print(f2)
        if f1==0 or f2==0:
            return "Balanced"
        if abs(f1-x)==abs(f2-x):
            return "Balanced"
        return "Not Balanced"



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    ob=Solution()
    print(ob.isBalanced(a,n,x))


# } Driver Code Ends