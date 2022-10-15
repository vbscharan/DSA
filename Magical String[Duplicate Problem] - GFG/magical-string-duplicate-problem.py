#User function Template for python3
class Solution:
    def magicalString (ob,S):
        # code here 
        S=list(S)
        for i in range(len(S)):
            #print("Old:",i,end=",")
            S[i]=chr(122-(ord(S[i])%97))
            #print("New:",i)
        return ''.join(S)
        #return ord("z")

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.magicalString(S))
# } Driver Code Ends