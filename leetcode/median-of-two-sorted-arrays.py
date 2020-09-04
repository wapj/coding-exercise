"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

좀 더 빠르게 할 수 있을것 같은데 쉽지 않다.
"""
from typing import List


class Solution:
    def median(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        n, m = len(nums1), len(nums2)
        median_idx = (n + m - 1) // 2
        i = j = 0

        cnt = 0
        while cnt < n + m:
            a = b = None
            if i < n:
                a = nums1[i]

            if j < m:
                b = nums2[j]

            if a == 0 or (a and not b and b != 0) or (a and b and a < b):
                nums.append(a)
                i += 1
                cnt += 1
            elif b == 0 or b:
                nums.append(b)
                j += 1
                cnt += 1

        if len(nums) % 2 == 0:
            ans = (nums[median_idx] + nums[median_idx + 1]) / 2
        else:
            ans = nums[median_idx]
        return ans


if __name__ == '__main__':
    nums1 = [0, 0]
    nums2 = [0, 0]
    nums1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    nums2 = [0, 6]
    print(Solution().median(nums1, nums2))
    print(Solution().median([1,3,5,7], [2,4,6,8,10]))
