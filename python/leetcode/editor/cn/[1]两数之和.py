# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10362 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """暴力遍历 时间复杂度O(n^2) 空间复杂度O(1)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        """
        建立字典 lookup 存放第一个数字，并存放该数字的 index
        判断 lookup 中是否存在： target - 当前数字， 则表明 当前值和 lookup中的值加和为 target.
        如果存在，则返回： target - 当前数字 的 index 和 当前值的 index
        如果不存在 令lookup[当前数字]=[i]
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_up = {}
        for i, num in enumerate(nums):
            if target - num in look_up:
                return [i, look_up[target - num]]
            else:
                look_up[num] = i
# leetcode submit region end(Prohibit modification and deletion)
