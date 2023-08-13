#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        queue=[]
        heapq.heapify(queue)
        heapq.heappush(queue,(0,0))
        visited=[0]*V
        cost=0
        while queue:
            pair=heapq.heappop(queue)
            if visited[pair[1]]!=1:
                visited[pair[1]]=1
                cost+=pair[0]
                for neighbor in adj[pair[1]]:
                    heapq.heappush(queue,(neighbor[1],neighbor[0]))
        return cost


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends