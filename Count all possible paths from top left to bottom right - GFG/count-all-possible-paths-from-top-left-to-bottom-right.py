#User function Template for python3
class Solution:
	def numberOfPaths(self, m, n):
		# code here
		dp=[[-1 for _ in range(n)] for _ in range(m)]
		def cw(xcr,ycr):
		    #print(xcr,ycr)
		    if xcr<0 or xcr>m-1 or ycr<0 or ycr>n-1:
		        return 0
		    if xcr==0 and ycr==0:
		        return 1
	        if dp[xcr][ycr]!=-1:
	            return dp[xcr][ycr]
	        right=cw(xcr,ycr-1)
	        down=cw(xcr-1,ycr)
	        dp[xcr][ycr]=(right+down)%1000000007
	        return dp[xcr][ycr]
        return cw(m-1,n-1)
        #return cw.count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m=int(m)
		n=int(n)
		ob = Solution();
		print(ob.numberOfPaths(m,n))

# } Driver Code Ends