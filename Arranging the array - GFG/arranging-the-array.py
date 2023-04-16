#User function Template for python3

def Rearrange( a, n):
    # Your code goes here
    negin=0
    posin=0
    while posin<n:
        if a[posin]<0:
            #a[posin],a[negin]=a[negin],a[posin]
            a.insert(negin,a.pop(posin))
            posin+=1
            negin+=1
            #print(a)
        else:
            posin+=1
    
    
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Rearrange(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends