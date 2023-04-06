#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		# code here
		if n==1:
		    arr[-1]=-1
		i=0;j=i+1
		while j<n:
		    if arr[j]<arr[i]:
		        arr[i]=arr[j]
	        else:
	            arr[i]=-1
            i+=1;j+=1
        arr[-1]=-1
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends