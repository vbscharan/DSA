#User function Template for python3

# Function to check if elements are 
# pairwise consecutive in stack 
def pairWiseConsecutive(l):
    
    #add code here
    if len(l)%2==0:
        pass
    else:
        l.pop()
    while len(l):
        x=l.pop()
        y=l.pop()
        if abs(x-y)==1:
            continue
        else:
            return 0
    return 1
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        if(pairWiseConsecutive(l)==True):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends