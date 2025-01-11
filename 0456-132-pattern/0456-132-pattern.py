class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
       
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]<nums[j] and nums[j]>nums[k] and nums[k]>nums[i]:
        #                 return True
        # return False 

        stack = []
        currMin =nums[0]
        for n in nums[1:]:
            while stack and n>=stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True
            stack.append([n,currMin])
            currMin = min(currMin,n)
        return False
