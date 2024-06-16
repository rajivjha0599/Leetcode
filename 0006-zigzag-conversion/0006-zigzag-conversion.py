class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['']*numRows
        cur_row = 0
        goingDown = False
        if numRows==1:
            return s
        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0 or cur_row == numRows-1:
                goingDown =not goingDown
            if goingDown:
                cur_row += 1
            else:
                cur_row -= 1
        return "".join(rows)
            
        