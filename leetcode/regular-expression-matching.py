"""
10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

s = "aa"
p = "a"
Output: false

s = "aa"
p = "a*"
Output: true

s = "ab"
p = ".*"
Output: true

s = "aab"
p = "c*a*b"
Output: true

s = "mississippi"
p = "mis*is*p*."
"""

"""
재귀를 사용하기
* 가 없이 . 만 있는 경우는 쉽다.

재귀로 한글자씩 가면 됨
def is_match(s: str, p: str) -> bool:
    if not p:
        return not s
    first_match = bool(s) and p[0] in [s[0], "."]    
    return first_match and is_match(s[1:], p[1:])
    
*가 붙는 경우는 아래와 같이 해결가능

```python 
def is_match(s: str, p: str) -> bool:
    if not p:
        return not s
    first_match = bool(s) and p[0] in [s[0], "."]

    if len(p) >= 2 and p[1] == '*':
        return is_match(s, p[2:]) or first_match and is_match(s[1:], p)
    else:
        return first_match and is_match(s[1:], p[1:])
```
"""


def is_match(s: str, p: str) -> bool:
    if not p:
        return not s
    first_match = bool(s) and p[0] in [s[0], "."]

    if len(p) >= 2 and p[1] == '*':
        return is_match(s, p[2:]) or first_match and is_match(s[1:], p)
    else:
        return first_match and is_match(s[1:], p[1:])



