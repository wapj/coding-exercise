"""
8. String to Integer (atoi)
Implement atoi which converts a string to an integer.

' '만 화이트 스페이스로 친다.
ange: [−2**31,  2**31 − 1] 범위의 수만 출력가능

+,-,숫자가 아닌 것으로 시작하면 0
"""
import re


class Solution:
    def atoi(self, s: str) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        arr = list(s.strip())
        if len(arr) == 0: return 0

        sign = -1 if arr[0] == '-' else 1
        if arr[0] in ['-', '+']: del arr[0]
        ret, i = 0, 0
        while i < len(arr) and arr[i].isdigit():
            ret = ret * 10 + ord(arr[i]) - ord('0')
            i += 1

        return max(MIN, min(sign * ret, MAX))


print(Solution().atoi(" "))
