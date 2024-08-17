class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1
        while l!=r:
            #print(min(height[l],height[r])) 
            water = (r-l)*((min(height[l],height[r])))
            if water>ans:
                ans= water
            if(height[l]<height[r]):l+=1
            else:r-=1
        return ans