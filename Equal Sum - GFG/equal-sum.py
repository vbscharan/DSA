#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
    	# code here
    	l=sum(arr)
    	r=0
    	i=n-1
    	#l-=arr[-1]
    	while i>=0:
    	    l-=arr[i]
    	    if l==r:
    	        return "YES"
	        else:
	            #if i+1<n:
	            i-=1
	            r+=arr[i+1]
	            
            #i-=1
        return "NO"
	            
	            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends