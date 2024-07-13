

class Solution:
    def helper(self, seq):
        if len(seq) <= 1:
            return seq
        pivot = seq[-1]
        small = []
        large = []
        
        for num in seq[:-1]:
            if int(str(num) + str(pivot)) > int(str(pivot) + str(num)):
                large.append(num)
            else:
                small.append(num)
        return self.helper(large) + [pivot] + self.helper(small)
    
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        sorted_nums = self.helper(nums)
        # Concatenate the numbers and handle leading zeros
        largest_num = ''.join(map(str, sorted_nums))
        return '0' if largest_num[0] == '0' else largest_num
