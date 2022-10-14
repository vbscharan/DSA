class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	k=[0]*n
    	for i in arr:
    	    k[i]+=1
	    if any(k[i] for i in range(len(k)) if k[i]>1):
	        return [i  for i in range(len(k)) if k[i]>1]
        else:
            return [-1]
	        
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends