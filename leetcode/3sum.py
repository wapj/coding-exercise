from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = set()
        for i, n in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            while(r > l):
                total = n + nums[l] + nums[r]
                if total == 0:

                    arr.add((n, nums[l], nums[r]))
                    l +=1
                    print(n, nums[l])
                    if nums[l] == n:
                        break
                    r -=1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return list(arr)

## set을 사용해서 유일한 배열을 출력하는 것은 했는데, 너무 느리다. 

s = Solution()

nums = [-1, 0, 1, 2, -1, -4]

result = s.threeSum(nums)
print(result)
