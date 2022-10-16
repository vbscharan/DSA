#User function Template for python3
class Solution:
    def sumOfTheSeries (self, n):
        # code here 
        return n*(n+1)*(2*n+1)//6


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfTheSeries(n))
# } Driver Code Ends