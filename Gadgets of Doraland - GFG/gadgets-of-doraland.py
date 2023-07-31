#User function Template for python3
import heapq
class Solution:
    def TopK(self, array, k):
        # code here
        '''
        dic={}
        heap=[]
        for i in array:
            dic[i]=dic.get(i,0)+1
        for i in set(array):
            heapq.heappush(heap,(-1*dic[i],-1*i))
        for i in range(k):
            yield -1*heapq.heappop(heap)[1]
        '''
        dic={}
        heap=[]
        for i in array:
            dic[i]=dic.get(i,0)+1
        for i in set(array):
            heap.append([-1*dic[i],-i])
        heapq.heapify(heap)
        for i in range(k):
            yield -1*heapq.heappop(heap)[1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        res = obj.TopK(array, k)
        for each in res:
            print(each, end=' ')
        print()

# } Driver Code Ends