# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。# 数组中的每个元素代表你在该位置可以跳跃的最大长度。# 判断你是否能够到达最后一个下标。

case1 = [3,1,2,0,5]
case2 = [3,2,1,0,4]
#case2 = [3]
#case4 = 

def func(nums):
    if not nums:
        return None
    
    length = len(nums)
    stack = []
    i = 0
    r = i + nums[0]

    while i < length:
        r = max(r, nums[i] + i) 
        if r > length - i:
            return True 
        i += 1
    return False

func(case2)