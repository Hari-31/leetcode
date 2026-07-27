class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        win = set()
        for right in range(len(nums)):
            if right - left > k:
                win.remove(nums[left])
                left +=1

            if nums[right] in win:
                return True
            win.add(nums[right])

        return False

        