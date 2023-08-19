#User function Template for python3
class Solution:
    def check(self, N, M, Edges): 
        #code here
        graph={}
        for i in range(1,N+1):
            graph[i]=[]
        for i in Edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        def dfs(current_vertex):
            visited[current_vertex] = True
            if all(visited[1:]):
                return True
            for neighbor in graph[current_vertex]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            visited[current_vertex] = False
            return False
        for i in range(1,N+1):
            visited=[0]*(N+1)
            if dfs(i):
                return 1
        return 0
               


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends