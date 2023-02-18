#User function Template for python3

#_push function to insert elements of array to stack
def _push(arr):
    #return a stack with all elements of arr inserted in it
    return arr
    

#_pop function to print elements of the stack remove as well
def _pop(stack):
    #print top and pop for each element until it becomes empty
    if len(stack)==0:
        return
    print(stack.pop(),end=" ")
    _pop(stack)
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr=[int(i) for i in input().split()]
        stack = _push(arr)
        _pop(stack)
        print()

# } Driver Code Ends