import heapq
import sys
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        visited=[0]*V
        dis=[10000000]*V
        dis[S]=0
        heap=[]
        heapq.heapify(heap)
        heapq.heappush(heap,(0,S))
        while heap:
            pair=heapq.heappop(heap)
            weight=pair[0]
            sourceVertex=pair[1]
            if visited[sourceVertex]!=1:
                visited[sourceVertex]=1
                for neighbor in adj[sourceVertex]:
                    destVertex=neighbor[0]
                    cost=neighbor[1]
                    if visited[destVertex]!=1 and (dis[destVertex]>dis[sourceVertex]+cost):
                        dis[destVertex]=dis[sourceVertex]+cost
                        heapq.heappush(heap,(dis[destVertex],destVertex))
        return dis
                        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends