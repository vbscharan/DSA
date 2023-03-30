#User function Template for python3
class Solution:

	def checkTriplet(self,arr, n):
    	# code here
    	if n<=2:
    	    return False
	    else:
	        arr=sorted(arr)
	        #i=0;;j=k-1
            for k in range(n-1,0,-1):
                i=0;j=k-1
	            while i<j:
	                if arr[i]**2+arr[j]**2==arr[k]**2:
	                    return True
                    elif arr[i]**2+arr[j]**2>arr[k]**2:
	                    j-=1
                    else:
                        i+=1
            return False
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends