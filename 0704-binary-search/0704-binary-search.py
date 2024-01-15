class Solution:
    @staticmethod
    def bs(start,end,data:List[int],target):
        if (start>end):
            return -1

        middle = start + ((end-start) // 2)
        if(data[middle]==target):
                return middle
        elif (data[middle]>target):
                return Solution.bs(start,middle-1,data,target)
        elif (data[middle]<target):
                return Solution.bs(middle+1,end,data,target)
    def search(self, nums: List[int], target: int) -> int:
        return Solution.bs(0,len(nums)-1,nums,target)
        