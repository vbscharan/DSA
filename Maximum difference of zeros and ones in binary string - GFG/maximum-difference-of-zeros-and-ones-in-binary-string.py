#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		maxi=0
		zero=0
		one=0
		diff=0
		for i in S:
		    if i=='0':
		        zero+=1
	        elif i =='1':
	            one+=1
            if one>zero:
                one=zero=0
            if (zero-one)>diff:
                diff=(zero-one)
        if diff==0:
            return -1
        return diff
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends