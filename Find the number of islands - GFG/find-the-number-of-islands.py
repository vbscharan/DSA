#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        #code here
        n=len(grid)
        m=len(grid[0])
        di=((0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1))
        visited=[[0]*m for _ in range(n)]
        def dfs(sr,sc):
            if not visited[sr][sc]:
                visited[sr][sc]=1
                #print(sr,sc)
                for i in di:
                    nr=sr+i[0]
                    nc=sc+i[1]
                    if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1 and not visited[nr][nc]:
                        dfs(nr,nc)
                    
        startIndex=[]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    startIndex.append((i,j))
        count=0
        for pair in startIndex:
            if not visited[pair[0]][pair[1]]:
                count+=1
                dfs(pair[0],pair[1])
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends