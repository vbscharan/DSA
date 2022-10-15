#User function Template for python3

class Solution:    
    def Rearrange(self, a, n, answer):
        #Code Here
        a=sorted(a)
        #print(a)
        i=0;j=n-1
        l=0
        while(i<j):
            answer[l]=a[i]
            l+=1
            answer[l]=a[j]
            l+=1
            i+=1;j-=1
        if(n%2!=0):
            answer[l]=a[i]
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        answer = [0 for x in range(n)]
        ob = Solution()
        ob.Rearrange(a, n, answer)
        print(*answer)

        T -= 1


if __name__ == "__main__":
    main()






# } Driver Code Ends