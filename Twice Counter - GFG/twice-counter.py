#User function Template for python3

class Solution:
    def countWords(self,List, n):
        #code here
        dic={}
        for i in List:
            if dic.get(i) is None:
                dic[i]=1
            else:
                dic[i]+=1
        k=0
        for i in set(List):
            if dic[i]==2:
                k+=1
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
# } Driver Code Ends