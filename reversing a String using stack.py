# Python code below
# You will need this class for your solution. Do not edit it.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Complete the function definition for reverse_string.
# Use print("messages...") to debug your solution.
def reverse_string(my_string):
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type,
    # and build the solution by filling the bucket within a loop.
    reversed_string = ""

    s = Stack()
    for i in my_string:
        s.push(i)

    # Create a new stack
    while not s.is_empty():
        reversed_string += s.pop()


    # Iterate through my_string and push the characters onto the stack

    # Use a while loop with the exit condition that the stack is empty.
    # Within this loop, update reversed_string with characters popped off the stack.

    # Return the result


print(reverse_string("Aa"))
