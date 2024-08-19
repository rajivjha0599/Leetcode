class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        i=0
        initial_sum = sum(arr[:k])
        if(initial_sum/k>=threshold):ans+=1
        for r in arr[k:]:
            initial_sum -= arr[i]
            i+=1
            initial_sum+=r
            if(initial_sum/k>=threshold):ans+=1
        return ans
