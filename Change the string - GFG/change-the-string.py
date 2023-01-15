#User function Template for python3


class Solution:
    def modify(self, s):
        # code here
        k=ord(s[0])
        if k>=65 and k<=90:
            return s.upper()
        else:
            return s.lower()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
# } Driver Code Ends