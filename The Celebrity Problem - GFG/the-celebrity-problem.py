#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        ind=-1;c=0;tc=0
        for i in range(len(M)):
            k=0
            for j in range(len(M)):
                if M[i][j]==1:
                    c+=1
                    k=1
            #print(k)
            if k==0:
                ind=i
                tc+=1
            #print(ind)
        
        if c==0 or tc>1:
            return -1
        return ind


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends