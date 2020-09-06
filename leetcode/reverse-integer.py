from math import inf


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x >= inf or x <= -inf:
            return 0

        s = str(x)
        ans = ''

        is_minus = False
        if s[0] == '-':
            is_minus = True

        for x in reversed(s):
            if x == '0' and len(ans) > 0:
                ans += x
            elif x not in ['0', '-']:
                ans += x

        if is_minus:
            ans = '-' + ans

        int_ans = int(ans)
        if int_ans > 2 ** 31 or int_ans < -2 ** 31 - 1:
            return 0

        return ans