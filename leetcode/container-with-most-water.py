from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        if len(height) == 2:
            return min(height[left], height[right])

        i = 0
        while i < len(height):
            size = right - left
            tmp = min(height[left], height[right]) * size

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            ans = max(ans, tmp)
            i += 1
        return ans


s = Solution()
arr = [2, 3, 4, 5, 18, 17, 6]
print(s.max_area(arr))

arr = [1, 1]
print(s.max_area(arr))

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.max_area(arr))

arr = [1, 6, 5, 2, 5, 4, 3]
print(s.max_area(arr))

arr = [1, 3, 2, 5, 25, 24, 5]
print(s.max_area(arr))
