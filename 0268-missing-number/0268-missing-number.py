class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        dummy1=0
        dummy2=0
        for i in range(len(nums)):
            dummy1=dummy1+(i+1)
            dummy2=dummy2+nums[i]
        return dummy1-dummy2
            
            