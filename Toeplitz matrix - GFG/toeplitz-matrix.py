# You are required to complete this method
# Return True/False or 1/0
def isToepliz(lis, n, m):
    #code here
    for i in range(n):
        for j in range(m):
            if i-1>=0 and j-1>=0 and lis[i][j]!=lis[i-1][j-1]:
                return 0
    return 1


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)]for j in range(n)]
        k=0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k+=1
        if isToepliz(matrix, n, m):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa
# } Driver Code Ends