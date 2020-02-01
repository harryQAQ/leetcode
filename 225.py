from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)
        for _ in range(self.q.qsize() - 1): self.q.put(self.q.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        tmp = self.q.get()
        self.push(tmp)
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q.qsize()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()