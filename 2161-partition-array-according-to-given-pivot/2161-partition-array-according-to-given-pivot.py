class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        mid   = []
        for num in nums:
            if(num < pivot):
                small.append(num)
            elif (num == pivot):
                mid.append(num)
            else:
                large.append(num)
        
        nums[:] =  small +mid+ large
        return nums