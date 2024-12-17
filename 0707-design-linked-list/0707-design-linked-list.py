class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        print(self.size, index)
        node = self.head.next

        if index >= self.size:
            return -1 

        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head.next

        if index > self.size:
            return
        
        for _ in range(index):
            node = node.next

        new_node = ListNode(val)
        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:        
        if index >= self.size:
            return
        
        node = self.head.next

        for _ in range(index):
            node = node.next

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)