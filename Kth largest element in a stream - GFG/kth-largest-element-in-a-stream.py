#User function Template for python3
import heapq
class Solution:
    def kthLargest(self, k, arr, n):
        # code here 
        heap=[]
        heapq.heapify(heap)
        m=[]
        for i in arr:
            if len(heap)<k:
                heapq.heappush(heap,i)
            else:
                if i>heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,i)
            if len(heap)>=k:
                m.append(heap[0])
            else:
                m.append(-1)
        return m
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,n=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(*ob.kthLargest(k,arr,n))
# } Driver Code Ends