class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = 0
        l, r = 0, len(matrix[0])-1
        for i in range(len(matrix)):
            if matrix[i][-1] == target or i and matrix[i][-1] >= target > matrix[i-1][-1]:
                print(i)
                y = i
                break
        while l<=r:
            mid = l+(r-l)//2
            
            if target > matrix[y][mid]:
                l = mid+1
            elif target < matrix[y][mid]:
                r = mid-1
            else:
                return True

        return False               