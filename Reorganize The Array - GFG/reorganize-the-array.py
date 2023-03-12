#User function Template for python3

def Rearrange (arr,  n) : 
    #Complete the function
    i=0
    while i<n:
        if arr[i]==i or arr[i]==-1:
            i+=1
        else:
            arr[arr[i]],arr[i]=arr[i],arr[arr[i]]
    '''
    for i in range(n):
        if arr[i]!=i and arr[i]!=-1:
            arr[arr[i]],arr[i]=arr[i],arr[arr[i]]
        else:
            continue
        i-=1
    '''
    return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Rearrange(arr, n);
    print(*res)




# } Driver Code Ends