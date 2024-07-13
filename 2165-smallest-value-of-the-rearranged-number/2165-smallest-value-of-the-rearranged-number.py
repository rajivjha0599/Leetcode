class Solution:
    def helper(self, seq):
        if len(seq) < 1:
            return seq
        pivot = seq[-1]
        smaller = []
        larger = []
        for num in seq[:-1]:  
            if num <= pivot:
                smaller.append(num)
            else:
                larger.append(num)
        return self.helper(smaller) + [pivot] + self.helper(larger)
       
    def smallestNumber(self, num: int) -> int:
        neg = 0
        if num < 0:
            neg = 1
        elif num == 0:
            return num
        num = str(abs(num))
        data = [int(i) if neg == 0 else -1 * int(i) for i in num]
        
        data = self.helper(data)

        if data[0] == 0:
            for i in range(1, len(data)):
                if data[i] != 0:
                    data[0], data[i] = data[i], data[0]
                    break

        smallest_num_str = ''.join(map(str, [abs(x) for x in data]))
        smallest_num = int(smallest_num_str)

        return -smallest_num if neg == 1 else smallest_num