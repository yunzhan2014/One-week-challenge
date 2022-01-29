#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return True
        if len(nums) == 1: return True
        range = nums[0]
        for i, v in enumerate(nums):
            if i <= range:
                range = max(range, i+v)
            else:
                return False
        return True


# @lc code=end

