#User function Template for python3
import heapq
from typing import List
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, k : int) -> int:
        # code here
        graph=[[] for _ in range(n)]
        for i in flights:
            graph[i[0]-1].append((i[1]-1,i[2]))
        #print(graph)
        '''
        def checkSourceVertex():
            visited=[0]*n
            def d(src):
                visited[src]=1
                for neighbor in graph[src]:
                    if not visited[neighbor[0]]:
                        d(neighbor[0])
            d(k-1)
            if all(visited):
                return True
            return False
        if not checkSourceVertex():
            return -1
        '''
       
        def dijkistra(start):
            distance=[float('inf')]*len(graph)
            distance[start]=0
            visited=[0]*n
            heap=[]
            heapq.heapify(heap)
            heapq.heappush(heap,(distance[start],start))
            while heap:
                curr=heapq.heappop(heap)
                #visited[curr[1]]=1
                for neighbor in graph[curr[1]]:
                    if curr[0]+neighbor[1]<distance[neighbor[0]]:
                        distance[neighbor[0]]=curr[0]+neighbor[1]
                        heapq.heappush(heap,(distance[neighbor[0]],neighbor[0]))
                        #visited[neighbor[0]]=1
            return distance
        li=dijkistra(k-1)            
        #print(li)
        if float('inf') in li:
            return -1
        return max(li)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends