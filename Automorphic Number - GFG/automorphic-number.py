#User function Template for python3

class Solution:
	def is_AutomorphicNumber(self, n):
		# Code here
		sq=n*n
		while n!=0:
		    if sq%10!=n%10:
		        return "Not Automorphic"
	        sq//=10
	        n//=10
        return "Automorphic"



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_AutomorphicNumber(n)
		print(ans)
# } Driver Code Ends