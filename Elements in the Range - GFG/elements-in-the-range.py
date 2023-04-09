class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        dic={}
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in range(A,B+1):
            if dic.get(i)==None:
                return 0
            elif dic[i]>0:
                continue
            else:
                return 0
        return 1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l = list(map(int, input().split()))
        n=l[0]
        k=l[1]
        y=l[2]
        a = list(map(int,input().split()))
        ob = Solution()
        ans=ob.check_elements(a,n,k,y)
        if(ans):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends