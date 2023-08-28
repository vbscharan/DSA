

class Solution:
    
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		#Code here
		n=len(grid)
		m=len(grid[0])
		visited=[[0]*m for _ in range(n)]
		di=((0,1),(1,0),(0,-1),(-1,0))
		def dfs(sr,sc):
		    visited[sr][sc]=1
		    for i in di:
		        nr=i[0]+sr
		        nc=i[1]+sc
                if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]=='X':
                    dfs(nr,nc)
        #count+=1
        startIndex=[]
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='X':
                    startIndex.append((i,j))
        count=0
        for i in startIndex:
            if not visited[i[0]][i[1]]:
                count+=1
                dfs(i[0],i[1])
        return count
#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = [['#' for i in range(m)] for j in range(n)]
		for i in range(n):
			s = input().strip()
			for j in range(m):
				grid[i][j] = s[j]
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)
# } Driver Code Ends