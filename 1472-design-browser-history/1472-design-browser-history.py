class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = HistoryNode(None)
        self.tail = HistoryNode(None)

        self.curr = HistoryNode(homepage)
        self.curr.next = self.tail
        self.curr.prev = self.head

        self.head.next = self.curr
        self.tail.prev = self.curr

    def visit(self, url: str) -> None:
        new_node = HistoryNode(url)
        new_node.prev = self.curr  
        new_node.next = self.tail

        self.curr.next = new_node
        self.tail.prev = new_node

        self.curr = new_node

    def back(self, steps: int) -> str:
        num = 0
        while num < steps and self.curr.prev.url:
            self.curr = self.curr.prev
            num += 1

        return self.curr.url

    def forward(self, steps: int) -> str:
        num = 0
        while num < steps and self.curr.next.url:
            self.curr = self.curr.next
            num += 1

        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)