class Solution:
	def isWordExist(self, board, word):
		#Code here
		m=len(board[0])
		n=len(board)
		wlen=len(word)
		visited=[[0]*m for _ in range(n)]
		startIndex=[]
		for i in range(n):
		    for j in range(m):
		        if board[i][j]==word[0]:
		            startIndex.append((i,j))
        di=((0,1),(1,0),(-1,0),(0,-1))
        def wordSearch(sr,sc,ind):
            visited[sr][sc]=1
            '''
            if ind==(wlen-1):
                print("Word",word[ind],"Ind",ind)
                print(sr,sc)
                wordSearch.found=True
                return
            '''
            if board[sr][sc]==word[ind]:
                
                #print("Word",word[ind],"Ind",ind)
                #print(sr,sc)
                if ind==(wlen-1):
                    wordSearch.found=True
                    return
                for i in di:
                    nr=sr+i[0]
                    nc=sc+i[1]
                    if 0<=nr<n and 0<=nc<m and visited[nr][nc]==0 and not wordSearch.found:
                        #print("inside:",nr,nc)
                        wordSearch(nr,nc,ind+1)
            else:
                visited[sr][sc]=0
        wordSearch.found=False
        for i in startIndex:
            wordSearch(i[0],i[1],0)
            #print(wordSearch.found)
            if wordSearch.found:
                return True
            visited=[[0]*m for _ in range(n)]
            #print("start")
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends