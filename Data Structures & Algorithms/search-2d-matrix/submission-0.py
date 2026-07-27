class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        top, bottom = 0, row-1

        while top <= bottom:
            curr_row = (top + bottom) //2
            if target > matrix[curr_row][-1]:
                top = curr_row + 1
            elif target < matrix[curr_row][0]:
                bottom = curr_row - 1
            else:
                break
        
        if not top <= bottom:
            return False

        curr_row = (top + bottom) //2
        L, R = 0, col - 1
        while L<= R:
            M = (L+R)//2
            if target > matrix[curr_row][M]:
                L = M + 1
            elif target < matrix[curr_row][M]:
                R = M -1
            else:
                return True
        return False 
        