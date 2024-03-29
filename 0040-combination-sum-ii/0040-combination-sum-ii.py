class Solution:
    def helper(self,arr,index,target,ds,ans):
        if(target==0):
            ans.append(ds[:])
            return
        for i in range(index, len(arr)):
            if(i>index and arr[i]==arr[i-1]):continue
            if arr[i]>target:break
            
            ds.append(arr[i])
            self.helper(arr,i+1,target-arr[i],ds,ans)
            ds.pop()
       
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        self.helper(candidates,0,target,[],ans)
        return ans