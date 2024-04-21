class MyQueue:
    def __init__(self):
        self.stack1  = []
        self.stack2  = []

    def push(self, x: int) -> None:
        self.stack2.append(x)    
        
    def pop(self) -> int:
        if(self.stack2==[]):
            return False
        else:
            while len(self.stack2)>1:
                self.stack1.append(self.stack2.pop())
            ans = self.stack2.pop()
            if(self.stack1):
                 while self.stack1 != []:
                    self.stack2.append(self.stack1.pop())
            return ans

    def peek(self) -> int:
        if(self.stack2==[]):
            return False
        else:
            return self.stack2[0]

    def empty(self) -> bool:
        if(self.stack2==[] and self.stack1==[]):
            return True
        else:
            return False