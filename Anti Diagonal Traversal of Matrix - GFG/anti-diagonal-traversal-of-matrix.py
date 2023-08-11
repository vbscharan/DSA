#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        def getAntiDiagonals(matrix):
            n = len(matrix)
            anti_diagonals = []

    # Traverse the upper right half of the matrix
            for d in range(n):
                i, j = 0, d
                anti_diagonal = []
                while j >= 0:
                    anti_diagonal.append(matrix[i][j])
                    i += 1
                    j -= 1
                anti_diagonals.append(anti_diagonal)

    # Traverse the lower left half of the matrix (excluding the main diagonal)
            for d in range(1, n):
                i, j = d, n - 1
                anti_diagonal = []
                while i < n:
                    anti_diagonal.append(matrix[i][j])
                    i += 1
                    j -= 1
                anti_diagonals.append(anti_diagonal)

    # Flatten the anti-diagonals list into a single array
            result = [element for diagonal in anti_diagonals for element in diagonal]

            return result

# Example usage

        anti_diagonals = getAntiDiagonals(matrix)
        #print(anti_diagonals)
        return anti_diagonals
#This function will give you the desired output for the provided example and any other square matrix. Just replace the matrix variable with your desired input matrix.








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends