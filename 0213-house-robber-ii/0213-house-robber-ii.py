class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<2:
            return nums[0]
        def helper(nums,start,end):
            prev1=0
            prev2=0
            nums= nums[start:end+1]
            for house in nums:
                dp=max(prev1,prev2+house)
                prev2=prev1
                prev1=dp
            return prev1
        return max(helper(nums,0, len(nums) - 2),
               helper(nums,1, len(nums) - 1))
                
            