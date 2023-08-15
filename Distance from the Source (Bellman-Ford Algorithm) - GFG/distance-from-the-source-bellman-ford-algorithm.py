#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        distance=[100000000]*V
        distance[S]=0
        for i in range(V):
            for edge in edges:
                if distance[edge[0]]!=100000000 and distance[edge[0]]+edge[2]<distance[edge[1]]:
                    distance[edge[1]]=distance[edge[0]]+edge[2]
        for i in range(V):
            for edge in edges:
                if distance[edge[0]]!=100000000 and distance[edge[0]]+edge[2]<distance[edge[1]]:
                    return [-1]
        #print(distance)
        return distance


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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends