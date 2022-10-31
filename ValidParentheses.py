"""
4. Valid Parentheses:-

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
    valid.An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


# def is_valid(s):
#     if s == '':
#         return True
#     elif s == '()' or s == '()[]{}' or s == '{}' or s == '[]':
#         return True
#     else:
#         return False
#
# print(is_valid("(]"))

class Solution:
    def isValid(self, s: str) -> bool:
        pair = dict(('()', '[]', '{}'))
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif len(st) == 0 or x != pair[st.pop()]:
                return False
        return len(st) == 0
    print(isValid(self=None, s="{()}"))
