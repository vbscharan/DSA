#User function Template for python3

def searchPattern(st, pat):
    # code here
    if st.find(pat)!=-1:
        return 1
    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(t):
    st=input()
    pat=input()
    if (searchPattern(st, pat)):
        print("Present")
    else:
        print("Not present")
# } Driver Code Ends