class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        ans = 0
        for num in nums:
            if count[k-num]>0:
                count[k-num] -=1
                ans+=1
            else:
                count[num] += 1  
        
        return ans