from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		def dfs(adj,node,par):
	        dfs.visited[node]=1
	        for i in adj[node]:
	            if dfs.visited.get(i) is None:
		            if dfs(adj,i,node):
		                return True
                elif par!=i:
                    return True
            return False
		    
        dfs.visited={}
        for i in range(len(adj)):
            if dfs.visited.get(i) is None:
                if dfs(adj,i,-1):
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