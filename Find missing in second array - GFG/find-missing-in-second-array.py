#User function Template for python3



def findMissing(A,B,N,M):
    # code here
    #A=sorted(A)
    #B=sorted(B)
    dic={}
    for i in A:
        if dic.get(i)==None: 
            dic[i]=dic.get(i,0)+1
    for i in B:
        if dic.get(i)!=None and dic[i]==1:
            dic[i]=dic.get(i,0)+1
    #print(dic)
    for i in A:
        if dic[i]==1:
            yield i
    '''
    while i<len(B):
        if A[i]==B[j]:
            i+=1
            j+=1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1
        else:
            k.append(A[i])
            i+=1
    while i<len(A):
        k.append(A[i])
        i+=1
    print(k)
    return k
    '''


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ans=findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends