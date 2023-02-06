#User function Template for python3
class Solution:
    def replaceAll (ob, S, oldW, newW):
        # code here
        oldl=len(oldW)
        newl=len(newW)
        l=list(S)
        i=0
        while i< len(l):
            if l[i:i+oldl]==list(oldW):
                l[i:i+oldl]=list(newW)
                i+=(newl-1)
            else:
                i+=1
        return ''.join(l)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        oldW = input()
        newW = input()
        
        ob = Solution()
        print(ob.replaceAll(S, oldW, newW))
# } Driver Code Ends