# User function Template for Python3

class Solution:
    def maxLength(self, S):
        # code here
        stack=[-1]
        maxLen=0
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack):
                    maxLen=max(maxLen,i-stack[-1])
                else:
                    stack.append(i)
            #print(stack)
        return maxLen
                
            
                    


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends