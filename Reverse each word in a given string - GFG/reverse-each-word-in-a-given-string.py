#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        return '.'.join(i[::-1] for i in s.split("."))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends