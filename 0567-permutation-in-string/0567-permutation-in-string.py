class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1freq ={}
        s2freq ={}
        
        for ch in s1:
            s1freq[ch] = s1freq.get(ch,0)+1
        
        for i in range(len(s1)):
            s2freq[s2[i]] = s2freq.get(s2[i],0)+1
        
        if s1freq == s2freq : return True
        
        for i in range(1, len(s2) - len(s1) + 1):
            
            if s2freq[s2[i-1]] == 1:
                del s2freq[s2[i-1]]
            else:
                s2freq[s2[i-1]] -= 1
                
            if s2[i+len(s1)-1] in s2freq:
                s2freq[s2[i+len(s1)-1]] += 1
            else:
                 s2freq[s2[i+len(s1)-1]] = 1
            if s1freq == s2freq : return True
        return False
            
            