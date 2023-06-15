#User function Template for python3

#Function to reverse the queue.
def rev(q):
    #add code here
    stack=[]
    for i in range(q.qsize()):
        stack.append(q.get())
    #print(stack)
    #print(q)
    while stack:
        q.put(stack.pop())
    #print(q)
    return q

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
        q=rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends