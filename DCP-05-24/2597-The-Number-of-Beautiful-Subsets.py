class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def countBeautifulSubsets(nums, k, index, current):
            count = 0
            for i in range(index, len(nums)):
                canAdd = True
                for num in current:
                    if abs(num - nums[i]) == k:
                        canAdd = False
                        break
                if canAdd:
                    current.append(nums[i])
                    count += 1 + countBeautifulSubsets(nums, k, i + 1, current)
                    current.pop()
            return count

        return countBeautifulSubsets(nums, k, 0, [])
