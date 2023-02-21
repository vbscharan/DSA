#User function Template for python3
#from itertools import defaultdict
class Solution:
    def removeChars (ob, string1, string2):
        # code here
        dic={};k=[]
        for i in string1:
            if dic.get(i) is None:
                dic[i]=1
            else:
                dic[i]+=1
        for i in string2:
            if dic.get(i) is None:
                continue
            else:
                dic[i]=0
        for i in string1:
            if dic[i]==0:
                continue
            else:
                k.append(i)
        return ''.join(k)
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()
        
        ob = Solution()
        print(ob.removeChars(string1,string2))
# } Driver Code Ends