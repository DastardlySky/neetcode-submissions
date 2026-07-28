class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2 
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        row = matrix[row]

        left = 0
        right = COLUMNS - 1

        while left <= right:
            mid = (left + right) //2
            if target > row[mid]:
                left = mid + 1
            elif target < row[mid]:
                right = mid -1
            else:
                return True

        return False  