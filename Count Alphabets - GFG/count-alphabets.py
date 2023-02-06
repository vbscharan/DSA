#User function Template for python3

class Solution:

    def Count(self, S):
        # code here
        k=0
        for i in S:
            if i.isalpha():
                k+=1
        return k
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.Count(S))
# } Driver Code Ends