#User function Template for python3
class Solution:
    def compareFive (ob,N):
        # code here 
        if N<5:
            return "Less than 5"
        elif N==5:
            return "Equal to 5"
        else:
            return "Greater than 5"
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.compareFive(N))
# } Driver Code Ends