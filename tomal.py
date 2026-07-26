class Stack:

    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1

sen=input("enter your preperable sentence=")
s=Stack()
rev=""
for word in sen:
    s.push(word)
while s.stack:
    tem=s.pop()
    rev=rev+tem
print(rev)