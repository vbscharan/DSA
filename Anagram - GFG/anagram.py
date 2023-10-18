#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        dicA={}
        dicB={}
        for i in a:
            dicA[i]=dicA.get(i,0)+1
        for i in b:
            dicB[i]=dicB.get(i,0)+1
        if len(dicA)!=len(dicB):
            return 0
        for i in a:
            if dicA.get(i) is not None and dicB.get(i) is not None and dicA[i]==dicB[i]:
                continue
            else:
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends