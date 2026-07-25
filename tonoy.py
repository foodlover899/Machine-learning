class stack:
    def _init_ (self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return "empty stack"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "empty stack"
        return self.stack.peek()
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)


s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
print(s.pop())
s.display()
print(s.peek())
s.display()
print(s.is_empty())
print(s.size())
