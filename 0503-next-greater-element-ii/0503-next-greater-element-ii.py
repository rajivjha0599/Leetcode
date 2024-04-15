class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []

        for i in range(2 * len(nums) - 1):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                ans[stack.pop()] = nums[i % len(nums)]
            if i < len(nums):
                stack.append(i)

        return ans
                      
