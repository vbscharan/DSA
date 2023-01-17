#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        a=sorted(a)
        #sum=0
        return sum(i*a[i] for i in range(len(a)))%(1000000007)
            
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends