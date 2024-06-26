class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if a == nums[i-1] and i>0:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                threesum = a + nums[l] + nums[r]
                if(threesum<0):
                    l=l+1
                elif(threesum>0):
                    r=r-1
                else:
                    res.append([a,nums[l],nums[r]])
                    l=l+1
                    while nums[l] == nums[l-1] and l<r:
                        l=l+1
        return res