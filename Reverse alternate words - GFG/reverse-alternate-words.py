#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        # code here
        k=list(Str.split(" "))
        for i in range(len(k)):
            if(i%2!=0):
                k[i]=k[i][::-1]
        return ' '.join(k)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends