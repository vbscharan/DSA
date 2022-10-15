#User function Template for python3
class Solution:

	def subMatrixSum(self,arr, n, m, x1, y1, x2, y2):
		# code here
	    sum=0
		for i in range(x1-1,x2):
		    for j in range(y1-1,y2):
		        sum+=arr[i][j]
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3






if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        x1, y1, x2, y2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.subMatrixSum(arr, n, m, x1, y1, x2, y2)
        print(ans)
        tc -= 1

# } Driver Code Ends