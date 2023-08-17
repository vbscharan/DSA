class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		n=len(image);m=len(image[0])
		di=((0,-1),(-1,0),(1,0),(0,1))
		startColor=image[sr][sc]
		visited=[[0]*m for _ in range(n)]
        def dfs(sr,sc):
            if image[sr][sc]==startColor:
                image[sr][sc]=newColor
                visited[sr][sc]=1
            for i in di:
                x=sr+i[0];y=sc+i[1]
                if 0<=x<n and 0<=y<m and image[x][y]==startColor and  not visited[x][y]:
                    dfs(x,y)    
        dfs(sr,sc)
        return image
            

#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends