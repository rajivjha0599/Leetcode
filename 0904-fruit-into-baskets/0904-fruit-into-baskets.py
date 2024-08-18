class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        data = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(fruits)):
            data[fruits[r]] +=1
            while(len(data)>2):
                data[fruits[l]]-=1
                
                if(data[fruits[l]]==0):
                    del data[fruits[l]]
                l+=1
            ans = max(ans,r-l+1)
        return ans