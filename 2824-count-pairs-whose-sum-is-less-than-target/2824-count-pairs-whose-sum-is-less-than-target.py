class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        ans=0
        nums.sort()
        while i<j:
            if(nums[i]+nums[j]<target):
                ans+=j-i
                i+=1
            else:
                j-=1
        return ans
                