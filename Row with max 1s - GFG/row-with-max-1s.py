#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		def BinarySearch(arr):
            l=0;h=len(arr)-1
            while l<=h:
                mid=(l+h)//2
                if arr[mid]>=1:
                    h=mid-1
                else:
                    l=mid+1
            return l
	    c=0;row=0        
		for i in range(n):
		    temp=arr[i][:]
		    k=BinarySearch(temp)
		    #print(k)
		    if (m-k)>c:
		        c=m-k
		        row=i
        if c==0:
            return -1
        return row 
	    '''
		    if k==0:
		        if arr[k]==0:
		            if len(temp)-1>c:
		                c=len(temp)-1
		                row=i
                else:
                    if len(temp)>c:
                        c=len(temp)
                        row=i
		    else:
		        if m-k>c:
		            c=(m-k)
		            row=i
            print("Row",row)
        '''
        
		    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends