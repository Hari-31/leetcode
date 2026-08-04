class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cl, cr = 0, len(matrix) -1
        rl, rr = 0, len(matrix[0]) -1
        mc, mr = 0,0
        while cl <= cr:
            mc = (cl + cr) // 2
            if mc > len(matrix) -1:
                break
            if matrix[mc][0] <= target <= matrix[mc][-1]:
                break
            if matrix[mc][0] > target:
                cr= mc -1
            else:
                cl = mc + 1

        while rl <= rr:
            mr = (rl + rr) // 2
            if mr > len(matrix[0]) -1:
                break
            if matrix[mc][mr] == target:
                return True
            if matrix[mc][mr] > target:
                rr= mr -1
            else:
                rl = mr + 1
        return False

