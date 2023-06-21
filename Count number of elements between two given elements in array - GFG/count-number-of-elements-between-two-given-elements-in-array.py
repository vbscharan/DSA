#User function Template for python3

class Solution:
    def getCount(self,arr, n, num1, num2): 
        #Comlete the function
        c=0
        i=0;j=n-1
        while i<=j:
            if arr[i]!=num1:
                i+=1
            if arr[j]!=num2:
                j-=1
            if arr[i]==num1 and arr[j]==num2:
                break
        if i==j:
            return 0
        return j-i-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    num1,num2 = map(int,input().strip().split())
    ob = Solution()
    v = ob.getCount(arr, n, num1, num2)
    print(v)
    
# } Driver Code Ends