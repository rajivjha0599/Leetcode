class BrowserHistory:

    def __init__(self, homepage: str):
        self.val = homepage
        self.next = None
        self.prev = None
        self.current = self
        
    def visit(self, url: str) -> None:
        new_page = BrowserHistory(url)
        new_page.prev = self.current
        self.current.next = new_page
        self.current = new_page
        

    def back(self, steps: int) -> str:
        while steps>0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps>0 and self.current.next is not None:
            self.current=self.current.next
            steps-=1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)