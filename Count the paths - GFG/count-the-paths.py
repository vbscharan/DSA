#User function Template for python3

class Solution:
    def possible_paths(self, edges, n, s, d):
        #Code here
        graph=[[] for _ in range(n)]
        for i in edges:
            if len(i):
                graph[i[0]].append(i[1])
        def dfs(graph,st,dt):
            if st==dt:
                dfs.count+=1
                return
            for neighbor in graph[st]:
                dfs(graph,neighbor,dt)
        dfs.count=0
        dfs(graph,s,d)
        return dfs.count
        
            
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, s, d = input().split()
		n = int(n); m = int(m); s = int(s); d = int(d);
		edges = []
		for _ in range(m):
		    x,y = input().split()
		    x = int(x); y = int(y);
		    edges.append([x,y])
		obj = Solution()
		ans = obj.possible_paths(edges, n, s, d)
		print(ans)


# } Driver Code Ends