# Understanding and Implementing the Stack Data Structure using Python

class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return not self.items

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        try:
            return self.items[-1]
        except Exception:
            return Exception

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()

    s.push(89)
    s.pop()
    s.peek()
    print(s)




