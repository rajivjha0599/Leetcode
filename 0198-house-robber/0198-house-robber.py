class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0
        for house in nums:
            dp = max(prev1,prev2+house)
            prev2=prev1
            prev1=dp
        return prev1