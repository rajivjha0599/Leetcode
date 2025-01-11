class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        idx1 = float('inf')
        idx2 = float('-inf')

        for i, num in enumerate(nums):
            while stack and num < stack[-1][0]:
                idx1 = min(idx1, stack.pop()[1])
            stack.append([num, i])
        
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while stack and num > stack[-1][0]:
                idx2 = max(idx2, stack.pop()[1])
            stack.append([num, i])
        
        if idx1 == float('inf') or idx2 == float('-inf'):
            return 0
        return idx2 - idx1 + 1
