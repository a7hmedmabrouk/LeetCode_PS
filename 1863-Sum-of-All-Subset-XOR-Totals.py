class Solution:
    def subsetXORSum(self, nums):
        def helper(index, current_xor):
            if index == len(nums):
                return current_xor
            return helper(index + 1, current_xor ^ nums[index]) + helper(index + 1, current_xor)
        
        return helper(0, 0)