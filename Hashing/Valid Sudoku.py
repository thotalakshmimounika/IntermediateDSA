# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.



# The input corresponding to the above configuration :

# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.

# Note:

# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, a):
        #row check
        for i in range(9):
            d={}
            c=0
            for j in range(9):
                if a[i][j] in d:
                    return 0
                elif a[i][j]!=".":
                    d[a[i][j]]=1
        #column check
        for j in range(9):
            d={}
            for i in range(9):
                if a[i][j] in d:
                    return 0
                elif a[i][j]!=".":
                    d[a[i][j]]=1
        #checking each box
        for i in range(0,9,3):
            for j in range(0,9,3):
                d={}
                for k in range(3):
                    for l in range(3):
                        x1=i+k
                        y1=j+l
                        if a[x1][y1] in d:
                            return 0
                        elif a[x1][y1]!=".":
                            d[a[x1][y1]]=1
        return 1
                    
#Time complexity = O(1)
#Space complexity - O(9)