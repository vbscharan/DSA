#User function Template for python3

class Solution:
    def splitString(ob, S): 
        # code here
        s1=[]
        s2=[]
        s3=[]
        for i in S:
            k=ord(i)
            if (k>=65 and k<=90) or (k>=97 and k<=122):
                s1.append(i)
            elif k>=48 and k<=57:
                s2.append(i)
            else:
                s3.append(i)
        #print(s1)
        return [''.join(s1),''.join(s2),''.join(s3)]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if(i==""):
                print(-1)
            else:
                print(i)


# } Driver Code Ends