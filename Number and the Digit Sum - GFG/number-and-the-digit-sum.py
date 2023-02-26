#User function Template for python3

class Solution:
    def numberCount(self,n,k):
    # code here
        l=1;h=n
        while l<=h:
            mid=(l+h)//2
            c=0
            while mid>0:
                c+=mid%10
                mid=mid//10
            mid=(l+h)//2
            if abs(mid-c)>=k:
                h=mid-1
            else:
                l=mid+1
        return n-h



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,k = ( int(x) for x in input().split() )
        ob = Solution()
        print(ob.numberCount(n,k))
# } Driver Code Ends