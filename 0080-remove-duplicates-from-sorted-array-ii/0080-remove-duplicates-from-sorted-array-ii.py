class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        count = defaultdict(int) 
        for n in nums:
            if count[n]<2:
                nums[i] = n
                i+=1
                count[n]+=1
        return i

