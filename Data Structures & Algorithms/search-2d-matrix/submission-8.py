class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        l, r = 0, len(matrix[-1])-1        
        y = 0

        top, bot = 0, len(matrix)-1
        
        while top <= bot:
            y = top+(bot-top) // 2
            print(y)
            if target > matrix[y][-1]:
                top = y + 1
            elif target < matrix[y][-1]:
                if target >= matrix[y][0]:
                    break
                bot = y - 1
            else:
                break

            
        while l<=r:
            x = l+(r-l)//2
            if matrix[y][x] < target:
                l = x+1
            elif matrix[y][x] > target:
                r = x-1
            else:
                return True           
        return False