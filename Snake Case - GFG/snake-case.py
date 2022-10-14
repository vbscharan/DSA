class Solution:
    def snakeCase(self, S , n):
        # code here
        return S.lower().replace(" ","_")

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        S=input()
        
        ob = Solution()
        print(ob.snakeCase(S , n))
# } Driver Code Ends