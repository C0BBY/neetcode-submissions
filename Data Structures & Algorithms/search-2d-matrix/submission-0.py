class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_sz, y_sz = len(matrix[-1]), len(matrix)
        l, r = 1, x_sz * y_sz

        while l <= r:
            mid = l + (r - l) // 2
            y_pos = math.ceil(mid / x_sz) - 1
            x_cell_no = (mid % x_sz)
            x_pos = (x_cell_no if x_cell_no else x_sz)-1
            mid_cell = matrix[y_pos][x_pos]

            if target > mid_cell:
                l = mid + 1
            elif target < mid_cell:
                r = mid - 1
            else:
                print(f"target::{target} found at::matrix[{y_pos}, {x_pos}]")
                return True
        return False