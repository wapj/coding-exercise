from typing import List

"""
https://leetcode.com/problems/sliding-window-maximum/
"""

class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        deque = []
        arr = []

        for i, n in enumerate(nums):

            # k개의 윈도우만 유지 되도록 한다. i가 증가될 때 deque의 0번에 있는 인덱스와 같으면 삭제한다.
            # i - q[0] == k 가 좀 헷갈릴 수 있는데, i, q[0], k 가 각각 3, 0, 3 이라면 아래와 같은 뜻이다.
            # i가 3이면 4번째 인덱스이고 q[0]은 0번째 인덱스이니 유효한 인덱스는 1,2,3 이므로 0번을 삭제하라는 뜻이다.
            if deque and i - deque[0] == k:
                deque.pop(0)

            # nums[i]의 값보다 작은 값들은 모두 삭제한다.
            # 이 과정을 반복함으로써 max값의 후보의 인덱스만 데크에 남게된다.
            while deque and n > nums[deque[-1]]:
                deque.pop()

            deque.append(i)

            # k 번째부터 결과 리스트에 최대값을 넣는다.
            if i >= k - 1:
                arr.append(nums[deque[0]])
        return arr


s = Solution()

nums = [3, -1, 1, 2, 7, 6, 5, 4]
k = 3
result = s.max_sliding_window(nums, k)
print(result)