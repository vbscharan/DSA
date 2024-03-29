#User function Template for python3
import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        heapq.heapify(A)
        count=1
        su=0
        while count<=K2:
            if K1<count<K2:
                su+=heapq.heappop(A)
            else:
                heapq.heappop(A)
            count+=1
            #heapq.heappop()
        return su
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        sz = [int(x) for x in input().strip().split()]
        k1, k2 = sz[0], sz[1]
        ob=Solution()
        print( ob.sumBetweenTwoKth(a, n, k1, k2) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends