#User function Template for python3
import heapq
def kthSmallest(mat, n, k): 
    # Your code goes here
    '''
    mat=[j for i in mat for j in i]
    heapq.heapify(mat)
    for i in range(k-1):
        #print(mat)
        heapq.heappop(mat)
    return heapq.heappop(mat)
    '''
    m=[]
    for i in range(len(mat[0])):
        heapq.heappush(m,(mat[i][0],i,0))
    for i in range(k-1):
        y=heapq.heappop(m)
        if y[2]<n-1:
            heapq.heappush(m,(mat[y[1]][y[2]+1],y[1],y[2]+1))
        
            
    return heapq.heappop(m)[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends