#User function Template for python3

class Solution:
	def findPeakElement(self, a):
		# Code here
		l=0;h=len(a)-1
		ma=a[0]
		while l<=h:
		    mid=(l+h)//2
		    if ma<a[mid]:
		        ma=a[mid]
		        l=mid+1
	        elif ma>a[mid]:
	            h=mid-1
            else:
                l=mid+1
                h=mid-1
		return ma    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		a = list(map(int,input().split()))
		ob = Solution();
		ans = ob.findPeakElement(a)
		print(ans)




# } Driver Code Ends