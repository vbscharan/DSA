#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        dic={}
        i=0;j=0;
        count=0
        ans=float('-inf')
        n=len(s)
        while j<n:
            dic[s[j]]=dic.get(s[j],0)+1
            if dic[s[j]]==1:
                count+=1
            if(count)<k:
                j+=1
            elif(count)==k:
                ans=max(ans,(j-i+1))
                j+=1
            else:
                while not count<=k:
                    dic[s[i]]-=1
                    if dic[s[i]]==0:
                        count-=1
                    i+=1
                j+=1
        if ans==float('-inf'):
            return -1
        return ans
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends