#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		if len(edges)==0:
		    return 0
		distance=[100000]*n
		distance[edges[0][0]]=0
		for _ in range(n):
		    for edge in edges:
		        if distance[edge[0]]!=100000 and distance[edge[0]]+edge[2]<distance[edge[1]]:
		            distance[edge[1]]=distance[edge[0]]+edge[2]
        for edge in edges:
		        if distance[edge[0]]!=100000 and distance[edge[0]]+edge[2]<distance[edge[1]]:
		            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends