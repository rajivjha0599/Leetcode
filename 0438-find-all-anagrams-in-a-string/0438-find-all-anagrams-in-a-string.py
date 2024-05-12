class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    #     ans=[]
    #     for i in range(len(s)):
    #         if sorted(p)==sorted(s[i:i+(len(p))]):
    #             ans.append(i)
    #     return ans
        if(len(s) < len(p)):
            return []
        p_freq ={}
        s_freq ={}
        ans =[]
        for ch in p:
            p_freq[ch] = p_freq.get(ch,0) + 1
        
        for i in range(len(p)):
            s_freq[s[i]] = s_freq.get(s[i],0) + 1
        
        if p_freq == s_freq:
            ans.append(0)
            
        for i in range(1, len(s) - len(p) + 1):
           
            if s_freq[s[i - 1]] == 1:
                del s_freq[s[i - 1]]
            else:
                s_freq[s[i - 1]] -= 1

           
            if s[i + len(p) - 1] in s_freq:
                s_freq[s[i + len(p) - 1]] += 1
            else:
                s_freq[s[i + len(p) - 1]] = 1
            
            if p_freq == s_freq:
                ans.append(i)
        return ans