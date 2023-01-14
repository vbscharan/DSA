#User function Template for python3

class Solution:
    def removeConsonants(self, s):
        #complete the function here
        k=''.join(i for i in s if  (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'))
        if len(k)>0 and len(k)<=len(s):
            return k
        return 'No Vowel'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.removeConsonants(s))
# } Driver Code Ends