from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if n == target:
                return nums[i - 1] + target + nums[i + 1]


s = Solution()

nums = [-1,2,1,-4]
target = 1
result = s.threeSumClosest(nums, target)

print(result)
