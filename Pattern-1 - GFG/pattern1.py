#User function Template for python3

class Solution:
    def findThePattern(self, N):
        # code here
        k=ord('A')
        m=[]
        for i in range(1,N+1):
            if(i==1 or i==N):
                o=[]
                for j in range(N):
                    o.append(chr(k))
                    k+=1
                m.append(''.join(o))
                    #print(chr(k),end="")
                    #k+=1
                #print()
            else:
                l=[]
                for j in range(N):
                    if j==0 or j==N-1:
                        l.append(chr(k))
                        k+=1
                    else:
                        l.append("$")
                m.append(''.join(l))
                #print()
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr=ob.findThePattern(N)
        for i in ptr:
            print(i)
# } Driver Code Ends