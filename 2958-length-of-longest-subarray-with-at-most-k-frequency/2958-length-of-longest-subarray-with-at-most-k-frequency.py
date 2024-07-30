class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        data = defaultdict(int)
        l=0
        for r in range(len(nums)):
            data[nums[r]]+=1
            while data[nums[r]] > k:
                data[nums[l]] -=1
                l+=1
            res=max(res,r-l+1)
        return res
            