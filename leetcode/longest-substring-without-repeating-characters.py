"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        sub = ""
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("longest-substring-without-repeating-characters.py"))


