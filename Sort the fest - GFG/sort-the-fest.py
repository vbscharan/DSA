#User function Template for python3


class Solution:
    def is_common(self, s, t):
        # Code here
        dic={}
        for i in s:
            dic[i]=0
        for i in t:
            if dic.get(i) is None:
                continue
            if dic[i]==0:
                return 'CHANGE'
        return 'BEHAPPY'
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = list(input().split())
		t = list(input().split())
		ob = Solution()
		ans = ob.is_common(s, t)
		print(ans)
# } Driver Code Ends