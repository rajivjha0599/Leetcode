class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeroes = 0
        l=0
        for r,num in enumerate(nums):
            if nums[r] == 0:
                zeroes+=1
            while zeroes ==2:
                if nums[l] == 0:
                    zeroes-=1
                l+=1
            ans = max(ans,r-l)
        return ans