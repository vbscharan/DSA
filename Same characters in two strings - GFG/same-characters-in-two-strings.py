#User function Template for python3

class Solution:

    def sameChar(self, A, B):
        # code here
        c=0
        for i in range(len(A)):
            if A[i]==B[i]:
                c+=1
            elif A[i].upper()==B[i].upper():
                c+=1
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        A = input().strip()
        B = input().strip()

        solObj = Solution()

        print(solObj.sameChar(A, B))

# } Driver Code Ends