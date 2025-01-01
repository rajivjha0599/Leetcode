class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices.copy()
        for i,num in enumerate(prices):
            while stack and prices[stack[-1]] >= num:
                ans[stack.pop()] -= num
            stack.append(i)
        return ans