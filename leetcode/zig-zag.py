"""
https://leetcode.com/problems/zigzag-conversion/
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        num = numRows

        for x in range(num):
            arr.append("")


        go_right = True
        idx = 0

        for ch in s:
            try:
                arr[idx] += ch
                if go_right:
                    idx += 1
                    if idx == num - 1:
                        go_right = False
                else:
                    idx -= 1
                    if idx == 0:
                        go_right = True
            except IndexError:
                if go_right:
                    idx -= 1
                else:
                    idx += 1
                arr[idx] += ch

        return "".join(arr)