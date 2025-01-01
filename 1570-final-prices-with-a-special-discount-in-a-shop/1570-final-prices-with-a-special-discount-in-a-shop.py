class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            flag = False
            for j in range(i+1,len(prices)):                
                if(prices[j]<=prices[i]):
                    flag = True
                    ans.append(prices[i] - prices[j])
                    break
            if flag == True:
                continue
            else:
                ans.append(prices[i])
        return ans
