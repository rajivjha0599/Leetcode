from collections import deque

class Solution:
    
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = deque(sandwiches)
        students = deque(students)
        ct = 0
        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                ct = 0

            else:
                students.append(students.popleft())
                ct+=1
            
            if(ct == len(students)):
                return len(students)
            
        return 0