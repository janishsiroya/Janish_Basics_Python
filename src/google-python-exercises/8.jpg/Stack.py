class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s = Stack()
print(s.size())
s.push(4)
s.push(5)
s.push(6)
s.push('jan')
s.push(True)
print(s.size())
print s.peek()
print s.pop()


