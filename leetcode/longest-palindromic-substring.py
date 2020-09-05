"""
5. Longest Palindromic Substring
"""


class Solution:

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s < 2:
            return s

        res = ""
        for i in range(len_s):
            # 홀수인 경우
            res1 = self.expand(s, i, i)
            if len(res1) > len(res):
                res = res1
            # 짝수인 경우
            res2 = self.expand(s, i, i+1)
            if len(res2) > len(res):
                res = res2
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
