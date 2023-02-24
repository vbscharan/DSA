#User function Template for python3
def BinarySearch(a,l,h,k):
    
    if l<=h:
        mid=(l+h)//2
        if a[mid]==k:
            return 1
        elif a[mid]<k:
            return BinarySearch(a,mid+1,h,k)
        else:
            return BinarySearch(a,l,mid-1,k)
    else:
        return 0
def check (arr,  brr, n) : 
    #Complete the function
    arr=sorted(arr)
    brr=sorted(brr)
    #print(arr)
    #print(brr)
    for i in range(n):
        if arr[i]==brr[i]:
            continue
        else:
            return 0
    return 1




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    brr = list(map(int,input().strip().split()))
    
    print(check(arr, brr, n))




# } Driver Code Ends