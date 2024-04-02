class Solution:
    def helper(self, nums, ds, visited, ans):
        if len(ds) == len(nums):
            ans.append(ds[:])  # Append a copy of ds, not ds itself
            return
        for i in range(len(nums)):
            if not visited[i]:
                ds.append(nums[i])
                visited[i] = True
                self.helper(nums, ds, visited, ans)
                ds.pop()
                visited[i] = False  # Corrected assignment

    def permute(self, nums):
        ans = []
        self.helper(nums, [], [False] * len(nums), ans)  # Initialize visited array
        return ans