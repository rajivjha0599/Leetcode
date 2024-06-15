class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
          return []

        ans = ['']
        digitToLetters = ['', '', 'abc', 'def', 'ghi',
                          'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for digit in digits:
            letters = digitToLetters[int(digit)]
            temp=[]
            for prefix in ans:
                for suffix in letters:
                    temp.append(prefix + suffix)
            ans = temp
        return ans    
                    
        