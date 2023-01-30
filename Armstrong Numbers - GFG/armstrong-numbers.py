#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here
        sum1=0
        k=n
        while n!=0:
            l=n%10
            sum1+=(l**3)
            n//=10
        #print(sum1)
        if sum1==k:
            return "Yes"
        return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends