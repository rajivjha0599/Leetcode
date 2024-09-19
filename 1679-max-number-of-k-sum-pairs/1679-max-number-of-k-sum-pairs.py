class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        temp = set()
        nums = sorted(nums)
        i = 0
        ans = 0
        j = len(nums) - 1
        while j>i:
            if nums[i]+nums[j] == k:
                if((i,j) not in temp):
                    temp.add((i,j))
                    ans+=1
                i+=1
                j-=1
            elif(nums[i]+nums[j]>k):
                j-=1
            else:
                i+=1
        return ans