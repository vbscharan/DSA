#User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        c=0
        arr=sorted(arr)
        dic={}
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in range(N):
            if dic[arr[i]]>1:
                c+=1
            else:
                for j in range(i):
                    if arr[i]%arr[j]==0:
                        c+=1
                        break
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends