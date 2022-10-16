#User function Template for python3

class Solution:
    def acceptedProposals (self,arr, n):
        # your code here
        mini=min(arr)
        maxi=max(arr)
        for i in arr:
            if i!=mini and i>mini and i<maxi:
                maxi=i
            #else:
            #    print("Mini:",i)
        m1=maxi
        mini=min(arr)
        maxi=max(arr)
        for i in arr:
            if i!=maxi and i<maxi and i>mini:
                mini=i
        m2=mini
        return m2,m1
               


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    res = ob.acceptedProposals (arr, n)
    print (res[0], end = " ")
    print (res[1])
# } Driver Code Ends