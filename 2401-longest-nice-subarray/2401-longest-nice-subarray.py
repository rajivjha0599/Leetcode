class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bitset = 0
        l=0
        ans = 0
        for r in range(len(nums)):
            while bitset&nums[r]!=0:
                bitset^=nums[l]
                l+=1
            bitset|=nums[r]
            ans = max(ans,r-l+1)
        return ans