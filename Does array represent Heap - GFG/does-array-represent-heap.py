
class Solution:
    def arrayRepresentHeap(self,arr,n):
        # Your code goes here            
        i=0
        l=(2*i)+1
        r=(2*i)+2
        while i<n:
            l=(2*i)+1
            r=(2*i)+2
            if l<n and arr[i]<arr[l]:
                return 0
            if r<n and arr[i]<arr[r]:
                return 0
            i+=1
        return 1
                


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(ob.arrayRepresentHeap(arr,n))
# } Driver Code Ends