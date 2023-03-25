#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		dic={}
		for i in nums:
		    dic[i]=dic.get(i,0)+1
	    return (i for i in sorted(dic.keys()) if dic[i]==1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends