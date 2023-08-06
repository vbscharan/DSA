from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def dfs(adj,node,parent):
		    dfs.visited[node]=1
		    for neighbor in adj[node]:
		        if dfs.visited.get(neighbor) is None:
		            if dfs(adj,neighbor,node):
		                return True
                elif parent!=neighbor:
                    return True
            return False
		
		dfs.visited={}
		for vertex in range(len(adj)):
		    if dfs.visited.get(vertex) is None:
		        if dfs(adj,vertex,-1):
		            return True
        return False
		    
#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends