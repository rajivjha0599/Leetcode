class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        ans = sum(nums[:k])
        temp = ans
        for r in nums[k:]:
            temp= (temp - nums[i] +r)
            ans = max(temp,ans)
            i+=1
        return ans/k