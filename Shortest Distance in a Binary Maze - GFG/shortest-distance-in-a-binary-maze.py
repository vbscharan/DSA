#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        if (grid[source[0]]==0 and grid[source[1]]==0) or (grid[destination[0]]==0 and grid[destination[1]]==0):
            return -1
        m=len(grid[0]);n=len(grid)
        visited=[[0]*m for _ in range(n)]
        direction=((0,1),(1,0),(0,-1),(-1,0))
        X=destination[0];Y=destination[1]
        queue=deque()
        queue.append((source[0],source[1],0))
        while queue:
            i,j,steps=queue.popleft()
            if i==X and j==Y:
                return steps
            for di in direction:
                r=i+di[0]
                c=j+di[1]
                if 0<=r<n and 0<=c<m and grid[r][c]!=0 and not visited[r][c]:
                    queue.append((r,c,steps+1))
                    visited[r][c]=1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends