#User function Template for python3

class Solution:
    def calc_Sum (self, arr,  n, brr, m) : 
        #Complete the function
        n1=n2=0
        for i in arr:
            n1=(n1*10)+i
        for i in brr:
            n2=(n2*10)+i
        return n1+n2
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.calc_Sum(arr, n, brr, m)
    print(res)


# } Driver Code Ends