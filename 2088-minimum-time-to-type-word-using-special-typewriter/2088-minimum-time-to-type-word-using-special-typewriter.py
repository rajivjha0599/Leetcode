class Solution:
    def minTimeToType(self, word: str) -> int:
        letter = 'a'
        moves = 0
        for ch in word:
            diff =  abs(ord(ch) - ord(letter))
            moves += min(diff,26-diff)
            letter = ch
        return moves+len(word)

