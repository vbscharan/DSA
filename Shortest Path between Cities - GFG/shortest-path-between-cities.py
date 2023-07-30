#User function Template for python3

class Solution:
    def shortestPath(self, x, y): 
        # code here
        count=0
        while x!=y:
            if x>y:
                x//=2
            else:
                y//=2
            count+=1
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		x,y = map(int,input().strip().split())
		ob = Solution()
		print(ob.shortestPath(x,y))
# } Driver Code Ends