#User function Template for python3
class Solution:
	def pattern(self, S):
		# code here
		k=[]
		for i in range(len(S)-1,-1,-1):
		    k.append(S[:i+1])
	    #print()
	    return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.pattern(S)
		for value in answer:
			print(value)
			

# } Driver Code Ends