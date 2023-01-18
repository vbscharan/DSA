#User function Template for python3

class Solution:
    def findTime(self, S1, S2):
        # code here 
        sum1=0
        current=0
        for i in S2:
            k=S1.index(i)
            sum1+=abs(current-k)
            current=k
            
        return sum1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1=input()
        S2=input()
        
        ob = Solution()
        print(ob.findTime(S1,S2))
# } Driver Code Ends