class Solution:
    def printMinIndexChar(self, s, patt):
		#Code here
		dic={}
		for i in range(len(s)):
	        if dic.get(s[i])==None:
		        dic[s[i]]=i
		        #print(s[i],dic[s[i]])
        #print(dic)
	    nini=len(s)
	    k=""
	    for i in patt:
	        #print(nini)
	        if dic.get(i)!=None and dic[i]<nini:
	            k=i
	            nini=dic[i]
        if k!="":
            return k
        else:
            return '$'
		    


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	S = input().strip()
    	patt = input().strip()
    	obj = Solution()
    	print(obj.printMinIndexChar(S, patt))
# } Driver Code Ends