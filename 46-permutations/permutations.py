class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                used[j] = True
                subset.append(nums[j])
                dfs()
                subset.pop()
                used[j] = False

        dfs()
        return res