#User function Template for python3
class Solution:
    def firstAndLast(self, a, n, x): 
        # Code here
        l=0;h=n-1
        first=-1
        while l<=h:
            mid=(l+h)//2
            if a[mid]<x:
                l=mid+1
                first=mid
            else:
                h=mid-1
        l=0;h=n-1
        second=-1
        while l<=h:
            mid=(l+h)//2
            if a[mid]>x:
                second=mid
                h=mid-1
            else:
                l=mid+1
        '''
        if first==-1 or second==-1:
            if a[0]!=x:
                return [-1]
            if a[-1]!=x:
                return [-1]
       ''' 
        #print("first:",first,"Second:",second)    
        if first==-1:
            if second==-1:
                return [str(0),str(n-1)]
            if (second-1)>0 and a[second]==x:
                return [str(0),str(second-1)]
            else:
                #return [str(0),str(second-1)]
                return [-1]
        if second==-1:
            if first==-1:
                return [str(0),str(n-1)]
            if (first+1)<n and a[first+1]==x:
                return [str(first+1),str(n-1)]
            else:
                #return [str(first+1),str(n-1)]
                return [-1]
        
        if abs(first-second)==1:
            return [-1]
        return [str(first+1),str(second-1)]
                
            
        #print(first,second)
        #return "1"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends