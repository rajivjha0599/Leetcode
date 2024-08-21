class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hehe = "aeiou"
        vowel_cnt = 0
        ans = 0 
        for ch in s[:k]:
            if(ch in hehe):
                vowel_cnt+=1   
            ans=max(ans,vowel_cnt)          
        l=0
        for i,ch in enumerate(s[k:]):
            if (ch in hehe):
                vowel_cnt+=1
            if (s[l] in hehe):
                vowel_cnt-=1
            ans=max(ans,vowel_cnt)          
            
            l+=1
        return ans