class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        tracker = []
        idx = 0
        for i in range(1,n+1):
            if(target[idx] == i):
                print(target[idx])
                ans.append("Push")
                tracker.append(i)
                idx+=1
                if tracker == target:return ans
            else:
                ans.append("Push")
                ans.append("Pop")

        return ans