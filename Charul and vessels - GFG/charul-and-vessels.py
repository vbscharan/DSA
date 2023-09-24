#User function Template for python3
import heapq
def vessel (arr, n, k) : 
    #Complete the function
    dp=[[0]*(k+1) for _ in range(n+1)]
    for i in range(k+1):
        dp[0][i]=False
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,k+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i][j-arr[i-1]] 
            else:
                dp[i][j]=dp[i-1][j]
    #for i in dp:
    #    print(i)
    #print(dp[n][k])
    return dp[n][k]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n, k = map(int,input().split())
    arr = list(map(int, input().strip().split()))
    ans = vessel(arr, n, k)
    if ans == True:
        print(1)
    else:
        print(0)





# } Driver Code Ends