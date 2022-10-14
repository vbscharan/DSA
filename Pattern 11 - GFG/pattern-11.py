#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        k=1
        if(N==1):
            print(1)
        else:
            for i in range(1,N+1):
                if(i%2==0):
                    k=0
                    for j in range(i):
                        print(k,end=" ")
                        if(k==1):
                            k=0
                        else:
                            k=1
                else:
                    k=1
                    for j in range(i):
                        print(k,end=" ")
                        if(k==1):
                            k=0
                        else:
                            k=1
                print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends