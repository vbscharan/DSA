#User function Template for python3
from collections import OrderedDict
class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        # code here
        dic=OrderedDict()
        ma=0
        for i in arr:
            dic[i]=dic.get(i,0)+1
            if ma<dic[i]:
                ma=dic[i]
        
        k=0
        for i in dic.keys():
            if dic[i]==ma:
                k=i
        #print(li)
        return k



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[x for x in input().strip().split()]
        obj = Solution()
        print(obj.mostFrequentWord(arr,n))

# } Driver Code Ends