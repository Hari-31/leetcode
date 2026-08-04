class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, u = 0, len(nums) -1
        while l < u:
            if nums[l] < nums[u]:
                return nums[l]
            mid = (l + u) // 2
            if nums[mid] > nums[u]:
                l = mid + 1
            else:
                u = mid

        return nums[l]





        