#User function Template for python3

class Solution:

    def findDiff(self, amount):
        # code here
        num2 = int(str(amount).replace('6','9'))
        return num2-amount


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        amount = int(input())

        solObj = Solution()

        print(solObj.findDiff(amount))
# } Driver Code Ends