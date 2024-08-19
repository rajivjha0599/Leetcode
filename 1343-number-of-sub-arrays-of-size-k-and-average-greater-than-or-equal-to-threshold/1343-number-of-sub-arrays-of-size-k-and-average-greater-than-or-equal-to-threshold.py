class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        required_sum = k * threshold  # Calculate the required sum in advance
        current_sum = sum(arr[:k])  # Initial sum of the first window

        if current_sum >= required_sum:
            ans += 1

        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]  # Slide the window by adding the next element and removing the first
            if current_sum >= required_sum:
                ans += 1

        return ans
