#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		a=[0]*26
		l=[]*len(S)
		for i in S:
		    if a[ord(i)%97]==0:
		        a[ord(i)%97]=1
        for i in S:
            if a[ord(i)%97]==1:
                a[ord(i)%97]=0  
                l.append(i)  
        return ''.join(l)
        
        #dic={}
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends