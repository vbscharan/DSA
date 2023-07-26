import heapq
class Solution:
    def minOperations(self, arr, n, k):
        # code here
        heapq.heapify(arr)
        count=0
        if arr[0]>=k:
            return 0
        while len(arr)>=2:
            count+=1
            #print(arr)
            k1=heapq.heappop(arr)
            k2=heapq.heappop(arr)
            heapq.heappush(arr,k1+k2)
            if arr[0]>=k:
                return count
            
        return -1


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = Solution().minOperations(arr, n, k)
        print(ans)
        tc -= 1


# } Driver Code Ends