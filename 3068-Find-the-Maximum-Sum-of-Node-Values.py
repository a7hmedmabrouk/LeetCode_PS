class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        N = len(nums)

        deltos = [(num ^ k) - num for num in nums]
        deltos.sort(reverse=True)
        
        total = sum(nums)
        best = total

        i = 0
        while i + 1 < N:
            total += deltos[i] + deltos[i + 1]
            best = max(best, total)
            i += 2

        return best