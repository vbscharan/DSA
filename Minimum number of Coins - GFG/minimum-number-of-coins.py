#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        denom=[1,2,5,10,20,50,100,200,500,2000]
        i=len(denom)-1
        k=[]
        while i>=0:
            if N>=denom[i]:
                k.append(denom[i])
                N-=denom[i]
            else:
                i-=1
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends