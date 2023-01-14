#User function Template for python3

class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		k=''.join(i for i in S if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) )
		if len(k)<=0:
		    return -1
	    return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.removeSpecialCharacter(S))


# } Driver Code Ends