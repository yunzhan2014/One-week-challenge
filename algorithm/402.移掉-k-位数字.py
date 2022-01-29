#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            if not stack:
                stack.append(i)
            elif int(i) >= int(stack[-1]):
                    stack.append(i)
            else:
                while int(stack[-1]) > int(i) and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(i)
        if k > 0:
            res = stack[:-k]
        else:
            res = stack
        return("".join(res).lstrip("0").lstrip('0'))
        #print(stack)

# @lc code=end