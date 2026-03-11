class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:
    def __init__(self, k: int):
        self.last = None
        self.capacity = k
        self.size = 0

    def insert(self, value: int):
        if self.last == None:
            new_node = Node(value)
            new_node.prev = new_node
            new_node.next = new_node
            self.last = new_node
        else:
            new_node = Node(value, self.last, self.last.next)
            self.last.next.prev = new_node
            self.last.next = new_node
        self.size += 1

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.insert(value)
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.insert(value)
        self.last = self.last.next
        return True

    def deleteHead(self):
        if self.size == 0:
            return False
        if self.size == 1:
            self.last = None
        else:
            self.last.next = self.last.next.next
            self.last.next.prev = self.last
        self.size -= 1
        
        return True

    def deleteFront(self) -> bool:
        return self.deleteHead()

    def deleteLast(self) -> bool:
        if self.last:
            self.last = self.last.prev
        return self.deleteHead()

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.last.next.val

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.last.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()