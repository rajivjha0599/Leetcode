class Solution:
    def combinationSumRecursion(self, i, current_combination, target, data, result):
        if target < 0:
            return
        elif target == 0:
            result.append(current_combination[:])
            return
        elif i >= len(data):
            return

        # Include the current element
        current_combination.append(data[i])
        self.combinationSumRecursion(i, current_combination, target - data[i], data, result)
        
        # Exclude the current element
        current_combination.pop()
        self.combinationSumRecursion(i + 1, current_combination, target, data, result)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumRecursion(0, [], target, candidates, result)
        return result
        