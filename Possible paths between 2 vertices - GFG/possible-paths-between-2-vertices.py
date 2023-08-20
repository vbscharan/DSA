#User function Template for python3

class Solution:
    
    #Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        # code here
        def dfs(src):
            #visited[src]=1
            if src==destination:
                #visited[src]=0
                dfs.count+=1
                return
            for neighbor in adj[src]:
                #if not visited[neighbor]:
                #print(src,neighbor)
                dfs(neighbor)
        dfs.count=0
        visited=[0]*V
        dfs(source)
        return dfs.count
#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for i in range(int(input())):
        V,E = map(int,input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u,v = map(int,input().split())
            adj[u].append(v)
        source,destination = map(int,input().split())
        ob = Solution()
        print(ob.countPaths(V,adj,source,destination))
        
# } Driver Code Ends