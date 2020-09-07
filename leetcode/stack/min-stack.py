"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x) -> None:
        self.stack.append(x)
        if self.min:
            if x < self.min[-1] and x != self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self) -> None:
        self.stack.pop()
        if self.getMin() not in self.stack:
            self.min = self.min[:len(self.min) - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.min[-1]

    def __repr__(self):
        return str(self.stack) + str(self.min)


"""
["MinStack","push","push","push","getMin","push","push","push","push","push","top","push","push","getMin","push","getMin","push","push","getMin","push","top","push","getMin","push","push","push","push","getMin","push","push","top","push","push","getMin","pop","getMin","push","push","getMin","getMin","push","getMin","pop","push","push","push","getMin","push","getMin","getMin","getMin","pop","getMin","push","push","getMin","top","getMin","push","getMin","getMin","getMin","getMin","push","getMin","getMin","getMin","push","getMin","push","getMin","push","getMin","getMin","getMin","getMin","pop","getMin","push","getMin","getMin","push","push","pop","push","getMin","push","top","top","push","push","getMin","pop","getMin","push","top","push","getMin","push","getMin","getMin"]
[[],[85],[-99],[67],[],[-27],[61],[-97],[-27],[35],[],[99],[-66],[],[-89],[],[4],[-70],[],[52],[],[54],[],[94],[-41],[-75],[-32],[],[5],[29],[],[-78],[-74],[],[],[],[-58],[-44],[],[],[-64],[],[],[-45],[-99],[-27],[],[-96],[],[],[],[],[],[26],[-58],[],[],[],[25],[],[],[],[],[33],[],[],[],[71],[],[-62],[],[-78],[],[],[],[],[],[],[-30],[],[],[85],[-15],[],[-40],[],[72],[],[],[18],[59],[],[],[],[-59],[],[10],[],[9],[],[]]
"""

stack = MinStack()
stack.push(85)
stack.push(-99)
stack.push(3)
stack.push(0)
stack.getMin()
print(stack)
stack.pop()
print(stack)
stack.getMin()
print(stack)
stack.pop()
stack.pop()
stack.getMin()
print(stack)
